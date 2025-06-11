from typing import List
from utils.types import Document

class BaseVectorStore:
    def __init__(self):
        # Initialize your vector store connection here
        pass

    def add_documents(self, documents: List[Document]):
        # Logic to insert documents into the vector store
        raise NotImplementedError("add_documents must be implemented by subclasses")
    
    def search_documents(self, query: str, top_k: int = 5) -> List[Document]:
        # Logic to search documents in the vector store
        raise NotImplementedError("search_documents must be implemented by subclasses")