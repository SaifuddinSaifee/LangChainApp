import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ["OPEN_API_KEY"] = apikey

st.title('GPT Creator with Langchain')
prompt = st.text_input('Plug in your prompt here')