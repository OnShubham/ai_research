from sentence_transformers import SentenceTransformer
from .split_chunking import text_spilter

def embedding():
    
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    
    embeddings = model.encode(text_spilter)
    
    return embeddings