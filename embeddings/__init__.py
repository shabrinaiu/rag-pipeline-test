from typing import List
from utils.types import Document

class BaseVectorStore:
    """
    Abstract base class for vector store implementations.
    Defines the interface for adding and searching documents.
    """
    def __init__(self):
        # Initialize your vector store connection here
        pass

    def add_documents(self, documents: List[Document]):
        """
        Insert a list of Document objects into the vector store.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("add_documents must be implemented by subclasses")
    
    def search_documents(self, query: str, top_k: int = 5) -> List[Document]:
        """
        Search for documents in the vector store relevant to the query string.
        Returns a list of Document objects.
        Must be implemented by subclasses.
        """
        raise NotImplementedError("search_documents must be implemented by subclasses")