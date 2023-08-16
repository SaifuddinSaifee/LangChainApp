# Building our own AutoGPT with the help of LangChain and GPT-3

Notes:

STREAMLIT - USED TO BUILD THE APP
LANGCHAIN- USED TO BUILD LLM WORKFLOW
OPENAI - NEEDED TO USE OPENAI GPT
WIKIPEDIA- USED TO CONNECT GPT TO WIKIPEDIA
CHROMADB - VECTOR STORAGE
TIKTOKEN - BACKEND TOKENIZER FOR OPENAI

## Run the app

Download the repo:
[Link](https://github.com/)

1. Install dependencies:
    pip install -r requirements.txt

2. Insert your GPT-3 apikey
    In the project directory, create a file `apikey.py` and paste in the following content

    ```python
    apikey = 'YOUR_OPENAI_API_KEY'
    ```

    Replace `YOUR_OPENAI_API_KEY` with your OpenAI key.

    Save the file.

    > [!IMPORTANT]
    > Make sure you add the `apikey.py` this file to `.gitignore`.

3. To run the code, type in terminal

    ```bash
    streamlit run app.py
    ```

## Types of use case

1. With user input prompts

use basic app.py
    ```bash
    streamlit run app.py
    ```


![Input prompts like ChatGPT](image.png)

2. Prompt templates

dynamic prompting

For example:

```
Write a conversational play on {topic}
```

The `Write a converstation play on` is part of the template, and `{topic}` is variable with user input from the user interface.

> You can change the prompt template to your own custom prompt on line number 19 of `app_pro_tem.py`

    ```bash
    streamlit run app_pro_tem.py
    ```

