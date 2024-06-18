# FastAPI Text Summarizer

## Setup

---

### 1. Create a virtual environment:

~~~
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
~~~

### 2. Install dependencies:

~~~
pip install -r requirements.txt
~~~

### 3. Set environment

#### Create a .env file in the root directory (AI_Pickles_Test_Task/.env) and add your OpenAI API key:

~~~
OPENAI_API_KEY=your_openai_api_key_here
~~~

## Run the application:

---

~~~
uvicorn main:app --reload
~~~

## Test the endpoint:

---

- Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.
- Or visit swagger http://127.0.0.1:8000/docs