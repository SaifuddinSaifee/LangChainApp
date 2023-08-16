import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = apikey

# App framkework
st.title('GPT Creator with Langchain')
prompt = st.text_input('Ask away!✨')

# LLMs
llm = OpenAI(temperature=0.9)

# Display input if there's a prompt
if prompt:
    response = llm(prompt)
    st.write(response)

