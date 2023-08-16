# This python file showcases the implementation of Buffer memory to our application
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

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

# Memory
memory = ConversationBufferMemory(input_key= 'topic', memory_key='chat_history')

# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=memory)

# Run multiple chains sequentially
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)


# Display input if there's a prompt
if prompt:
    response = sequential_chain({'topic': prompt})
    st.write(response['title'])
    st.write(response['script'])

    with st.expander('Message History'):
        st.info(memory.buffer)

