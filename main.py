import uvicorn

from fastapi import FastAPI, HTTPException
from langchain_text_splitters import RecursiveJsonSplitter

from models import TextToSummarize
from summarizer import create_summarizer_chain


# Initialize FastAPI app
app = FastAPI()

# Init chain
summarization_chain = create_summarizer_chain()

# Init splitter
splitter = RecursiveJsonSplitter(max_chunk_size=300)


@app.post("/summarize")
async def summarize(text_to_summarize: TextToSummarize):
    """
    Summarize the input text.
    :param text_to_summarize: Request body containing the text to summarize
    :return: Summarized text
    """
    try:
        # Create docs for chain
        chunks = splitter.create_documents(texts=[{"text": text_to_summarize.text}])

        # Generate summary using LangChain
        summary = summarization_chain.invoke(chunks)
        return {"summary": summary.get("output_text")}

    except Exception as e:
        # Handle any exception that occurs during summarization
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
