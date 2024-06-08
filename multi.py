from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

load_dotenv()
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_KEY)

model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')

def get_gemini_response(input, image, prompt):
  response = model.generate_content([{"text": input}, image[0], {"text": prompt}])
  return response.text


def input_image_details(uploaded_file):
  if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    image_parts = [{
      "mime_type": uploaded_file.type,
      "data": bytes_data
    }]

    return image_parts
  else:
    raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="MultiLamguage Invoice Extractor")

st.header("MultiLamguage Invoice Extractor")
input = st.text_input("Input Prompt", key = "input")
uploaded_file = st.file_uploader("Choose Image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the Image")

input_prompt="""
You are an expert in uderstanding images. We will upload a image and you have to answer any questions based on the uploaded image 
"""
if input:
  if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response is")
    st.write(response)
