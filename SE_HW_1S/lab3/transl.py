from fastapi import FastAPI, Request
from transformers import pipeline
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")

class Item(BaseModel):
    text: str

app = FastAPI()

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")

@app.post("/translate/")
def translate(item: Item):
    """I try something new"""
    
    return pipe(item.text)[0]

