# Evaluate RAG Pipeline using DeepEval
from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric, HallucinationMetric
from deepeval.test_case import LLMTestCase
from preprocessors import load_dataset
from embeddings.chroma import ChromaVectorStore
from generators.gemma_generator import GemmaGenerator
from pipelines import RagPipeline

# Prepare pipeline
vector_store = ChromaVectorStore()
dataset = load_dataset()
vector_store.add_documents(dataset)
rag_pipeline = RagPipeline(
    retriever=vector_store,
    generator=GemmaGenerator(model_name="google/gemma-2-8b"),
)

# Example evaluation data (replace with your own for real evaluation)
test_cases = [
    LLMTestCase(
        input="Explain the OWASP Top 10 for web applications.",
        actual_output=rag_pipeline.run("Explain the OWASP Top 10 for web applications."),
        retrieval_context=[doc.page_content for doc in dataset[:3]],
    ),
]

# Choose metrics for RAG evaluation
metrics = [
    AnswerRelevancyMetric(threshold=0.7),
    HallucinationMetric(threshold=0.3),
]

# Run evaluation
results = evaluate(test_cases, metrics)
print(results)
