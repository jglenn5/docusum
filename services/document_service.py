doc_list = []
def create_document(filename, user_id):
    doc = {
        "filename" : filename,
        "summary_text" : None,
        "user_id" : user_id,
        "created_at" : "10:05"
    }
    doc_list.append(doc)
    return doc



if __name__ == "__main__":
    result = create_document("contract.pdf", 1)
    print(result)