from services import ai_service
doc_list = []
def create_document(filename, user_id):
    doc = {
        "filename" : filename,
        "summary_text" : None,
        "user_id" : user_id,
        "created_at" : "10:05",
        "document_id" : len(doc_list)
    }
    doc_list.append(doc)
    return doc

def get_all_documents():
    return doc_list

def find_document_by_id(document_id):
    for document in doc_list:
        if document["document_id"] == int(document_id):
            return document   

def summarize_document(document_id):
    doc = find_document_by_id(document_id)
    summary = ai_service.summarize_text("Sample document content for testing")
    doc["summary_text"] = summary
    return doc 

if __name__ == "__main__":
    result = create_document("contract.pdf", 1)
    print(result)