from pydantic import BaseModel


class TextToSummarize(BaseModel):
    text: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "String that must be summarized",
                }
            ]
        }
    }