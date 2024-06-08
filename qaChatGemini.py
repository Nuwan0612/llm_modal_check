from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

load_dotenv()
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-latest')
chat = model.start_chat(history=[])

def get_gemini_response(question):
  response = chat.send_message(question, stream=True)
  return response

st.set_page_config(page_title="Q&A Demon")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
  st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if input and submit:
  response = get_gemini_response(input)
  st.session_state['chat_history'].append(("You",input))
  st.subheader("The response is")
  for chunk in response:
    st.write(chunk.text)
    st.session_state['chat_history'].append(("Bot",chunk.text))

st.subheader("Chat history")

for role,text in st.session_state['chat_history']:
  st.write(f"{role}:{text}")