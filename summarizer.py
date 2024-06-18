from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI


load_dotenv()


def create_summarizer_chain():
    # Initialize the OpenAI LLM using your OpenAI API key
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

    # Create a transformation chain for summarization
    summarization_chain = load_summarize_chain(llm=llm, chain_type="stuff")

    return summarization_chain
