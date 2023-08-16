# This python file uses Simple Sequential Chain
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ["OPENAI_API_KEY"] = apikey

# App framkework
st.title('GPT Creator with Langchain')
prompt = st.text_input('Ask away!✨')

# Prompt templates
title_template = PromptTemplate(
    input_variables= ['topic'],
    template='Write a YouTube video title on {topic}'
)

script_template = PromptTemplate(
    input_variables= ['title'],
    template='Write detailed creative script for a YouTube video with the TITLE: {title}'
)

# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)

# Run multiple chains sequentially
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True)


# Display input if there's a prompt
if prompt:
    response = sequential_chain.run(prompt)
    st.write(response)

