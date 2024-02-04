pip install transformers
import streamlit as st
from transformers import pipeline
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")

class Item(BaseModel):
    text: str


pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")

def translate(item: Item):
    return pipe(item.text)[0]

st.title("Translation App")
item = st.text_input("Enter text to translate:")
if st.button("Translate"):
    translated_text = translate(Item(text=item))
    st.success(f"Translated text: {translated_text}")

