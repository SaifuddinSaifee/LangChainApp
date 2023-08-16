# This python file uses Chains
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

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
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')

# Run multiple chains sequentially
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)


# Display input if there's a prompt
if prompt:
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['script'])


