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
    