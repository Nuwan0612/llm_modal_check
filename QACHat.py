from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

CLAUDE_KEY = os.getenv('ANTHROPIC_API_KEY')
CLAUDE_MODEL = "claude-3-opus-20240229"

import streamlit as st

def get_ai_response(question):
  chatllm = ChatAnthropic(temperature=0, api_key=CLAUDE_KEY, model_name=CLAUDE_MODEL)
  response = chatllm.invoke(question)
  return response

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ", key="input")


submit = st.button("Ask the question")

if submit:
  response = get_ai_response(input)
  st.subheader("The response is")
  st.write(response.content)