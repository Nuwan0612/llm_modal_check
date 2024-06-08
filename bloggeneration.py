import streamlit as st
from langchain.prompts import PromptTemplate
# from langchain_community.llms import Ollama

def getLLamaresponse(input_text, no_words, blog_style):
  # llm = Ollama(model="llama3")

  #Prompt Template
  template = """
    Write a blog for {blog_style} job profile a topic {input_text} within {no_words} words.
  """

  prompt = PromptTemplate(
    input_variables=[
      "blog_style",
      "input_text",
      "no_words"
    ],
    template=template
  )

  format_prompt = prompt.format(
    blog_style = blog_style,
    input_text = input_text,
    no_words = no_words
  )

  response = llm.invoke(format_prompt)

  return response


#
st.set_page_config(
  page_title="Generate Blogs",
  layout="centered",
  initial_sidebar_state="collapsed"
)

st.header("Generate Blogs")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
  no_words = st.text_input('No words to generate')

with col2:
  blog_style = st.selectbox(
    'Writing the blog for', 
    (
      'Reseachers',
      'Data Scientist',
      'Common People'
    ),
    index = 0
  )

submit = st.button("Generate")

if submit:
  st.write(getLLamaresponse(input_text, no_words, blog_style))