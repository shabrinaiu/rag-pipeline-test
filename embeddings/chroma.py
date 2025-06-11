import chromadb

from typing import List, Optional
from utils.types import Document
from . import BaseVectorStore
from sentence_transformers import SentenceTransformer


class ChromaVectorStore(BaseVectorStore):
    def __init__(
        self,
        collection_name: str = "rag_collection",
        persistent_path: Optional[str] = None,
    ):
        super().__init__()
        self.collection_name = collection_name
        # Initialize Chroma connection here
        self.chroma_client = (
            chromadb.PersistentClient(path=persistent_path)
            if persistent_path
            else chromadb.PersistentClient()
        )
        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, documents: List[Document]):
        print(
            f"Adding {len(documents)} documents to the Chroma vector store '{self.collection_name}'"
        )

        # Load model and send to GPU
        model = SentenceTransformer("all-MiniLM-L6-v2", device="cuda")

        for i in range(0, len(documents), 5000):
            batch = documents[i : i + 5000]
            print(f"Indexing batch {i} to {i+len(batch)}")

            ids = [f"doc_{i+j}" for j in range(len(batch))]
            texts = [doc.page_content for doc in batch]
            metas = [doc.metadata for doc in batch]
            embeds = model.encode(
                texts, batch_size=64, show_progress_bar=True, device="cuda"
            ).tolist()

            self.collection.add(
                ids=ids, documents=texts, metadatas=metas, embeddings=embeds
            )

    def search_documents(self, query: str, top_k: int = 3) -> List[Document]:
        print(
            f"Searching for '{query}' in the Chroma vector store '{self.collection_name}'"
        )

        results = self.collection.query(query_texts=query, n_results=top_k)

        return [
            Document(page_content=doc, metadata=metadata)
            for doc, metadata in zip(results["documents"][0], results["metadatas"][0])
        ]
