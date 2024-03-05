from fastapi import FastAPI, File, UploadFile, Response
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
from briarmbg import BriaRMBG
from utilities import postprocess_image, preprocess_image
import numpy as np
import io

from contextlib import asynccontextmanager


ai_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_path, net, device

    # Initiate the model
    model_path = "model.pth"
    net = BriaRMBG()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    net.load_state_dict(torch.load(model_path, map_location=device))
    net.to(device)
    net.eval()
    ai_models["net"] = net
    yield
    ai_models.clear()


app = FastAPI(lifespan=lifespan)

""" 
configure CORS and Middleware on the app 
so that faster whisper can return result 
without being blocked by the browser
"""
# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "null",
]

# Configure Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def inference(uploaded_image):
    model_input_size = [1024, 1024]
    orig_im = Image.open(io.BytesIO(uploaded_image))
    orig_im_np = np.array(orig_im)

    if orig_im_np.shape[2] == 4:
        orig_im_np = orig_im_np[:, :, :3]

    orig_im_size = orig_im_np.shape[0:2]
    image = preprocess_image(orig_im_np, model_input_size).to(device)

    result = net(image)
    result_image = postprocess_image(result[0][0], orig_im_size)

    pil_im = Image.fromarray(result_image)
    no_bg_image = Image.new("RGBA", pil_im.size, (0, 0, 0, 0))
    no_bg_image.paste(orig_im, mask=pil_im)

    buffered = io.BytesIO()
    no_bg_image.save(buffered, format="PNG")
    return buffered.getvalue()


@app.post("/remove_bg/")
async def remove_bg(file: UploadFile = File(...)):
    contents = await file.read()
    result_image = inference(contents)
    return Response(content=result_image, media_type="image/png")
