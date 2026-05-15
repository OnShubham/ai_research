from langchain_text_splitters import RecursiveCharacterTextSplitter
from .load_file import load_document

def text_spilter():
    
    text_spilter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    
    chunks = text_spilter.split_documents(load_document)
    
    return chunks