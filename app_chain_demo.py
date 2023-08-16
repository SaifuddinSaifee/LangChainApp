# This python file uses prompt templates
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = apikey

# App framkework
st.title('GPT Creator with Langchain')
prompt = st.text_input('Ask away!✨')

# Prompt template
title_template = PromptTemplate(
    input_variables= ['topic'],
    template='Write a conversational play script with atleast 10 dialogues on {topic}'
)

# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# Display input if there's a prompt
if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)

