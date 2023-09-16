# This python file uses Sequential Chain
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ["OPENAI_API_KEY"] = apikey

# App framkework
st.title('Blog Creator Creator (Title and Script)')
prompt = st.text_input('Advance prompts with Sequential Chain. Input the topic, and get a blog title + topic✨')

# Prompt templates
title_template = PromptTemplate(
    input_variables= ['topic'],
    template='Write a creative and tacky and unique blog title on {topic}'
)

script_template = PromptTemplate(
    input_variables= ['title'],
    template='Write a highly structured and detailed SEO optimized blog on TITLE: {title}, Make sure you first create a table content with atleast five headings and then write the blog according to table of content.'
)

# LLMs
llm = OpenAI(temperature=0.9, max_tokens=2000, streaming=True)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')

# Run multiple chains sequentially
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)


# Display input if there's a prompt
if prompt:
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['script'])


