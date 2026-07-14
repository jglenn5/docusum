from fastapi import FastAPI
from services import document_service

app = FastAPI()

@app.post("/documents")
def create_document_endpoint():
    return document_service.create_document("contract.pdf", 1)

@app.get("/documents")
def get_document_endpoint():
    return document_service.get_all_documents()