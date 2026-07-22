from fastapi import FastAPI
from services import document_service

app = FastAPI()

@app.post("/documents")
def create_document_endpoint():
    return document_service.create_document("contract.pdf", 1)

@app.get("/documents")
def get_document_endpoint():
    return document_service.get_all_documents()

@app.put("/documents/{document_id}/summarize")
def summarize_document_endpoint(document_id):
    return document_service.summarize_document(document_id)

