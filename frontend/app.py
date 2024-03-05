import streamlit as st
import requests
from PIL import Image
import io


def process_image(uploaded_file):
    if uploaded_file is not None:
        with st.spinner("Processing image..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://backend:8000/remove_bg/", files=files)

            if response.status_code == 200:
                try:
                    processed_image = Image.open(io.BytesIO(response.content))
                    st.session_state.processed_image = processed_image
                except Exception as e:
                    st.error(f"Error processing image: {e}")
            else:
                st.error(
                    f"Failed to process image. Status code: {response.status_code}"
                )


def main():
    st.set_page_config(
        page_title="background removal",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("AI Background Removal App")
    uploaded_image = st.session_state.get("uploaded_image", None)

    # Sidebar
    st.sidebar.title("Options")
    file_uploader_key = "file_uploader_" + str(hash("file_uploader"))
    uploaded_file = st.sidebar.file_uploader(
        "Upload an image", key=file_uploader_key, type=["png", "jpg", "jpeg"]
    )
    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file)
        st.session_state.uploaded_image = uploaded_image
        process_button_key = "process_button_" + str(hash("process_button"))
        if st.sidebar.button("Process Image", key=process_button_key):
            process_image(uploaded_file)

    # Main content area
    col1, col2 = st.columns(2)
    with col1:
        if uploaded_image is not None:
            st.subheader("Original Image")
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    with col2:
        processed_image = st.session_state.get("processed_image", None)
        if processed_image is not None:
            st.subheader("Processed Image")
            st.image(processed_image, caption="Processed Image", use_column_width=True)


if __name__ == "__main__":
    main()
