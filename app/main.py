from datetime import datetime
from fastapi import FastAPI
import spacy
import json

nlp = spacy.load('en_core_web_sm')

app = FastAPI()

@app.get("/")
def root(text:str):
    doc = nlp(text)
    response = {}
    labels = [ent.label_ for ent in doc.ents]
    for label in labels:
        response[label] = []

    for ent in doc.ents:
        response[ent.label_].append(ent.text)

    return response
