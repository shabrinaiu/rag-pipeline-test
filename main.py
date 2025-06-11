# Import Package
from preprocessors import load_dataset
from embeddings.chroma import ChromaVectorStore
from generators.gemma_generator import GemmaGenerator
from pipelines import RagPipeline

dataset = load_dataset()

vector_store = ChromaVectorStore()
vector_store.add_documents(dataset)

rag_pipeline = RagPipeline(
    retriever=vector_store,
    generator=GemmaGenerator(model_name="google/gemma-2-8b"),
)

question = "Explain the OWASP Top 10 for web applications."
response = rag_pipeline.run(question)
print(f"Question: {question}\nResponse: {response}")

# Chat LLM with memory manager
