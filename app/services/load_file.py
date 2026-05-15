from langchain_community.document_loaders.pdf import PyPDFLoader

def load_document(file):
    
    load_document = PyPDFLoader(file)
    
    documents = load_document.load()
    
    return documents
    