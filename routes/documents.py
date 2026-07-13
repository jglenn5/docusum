from fastapi import FastAPI
from services import document_service

app = FastAPI()

@app.post("/documents")
def create_document_endpoint():
    return document_service.create_document("contract.pdf", 1)