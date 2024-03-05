FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

LABEL maintainer="georgemountain"

WORKDIR /app

COPY requirements.txt app/requirements.txt

COPY . /app

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

