from typing import Optional
from embeddings import BaseVectorStore
from generators import LLMGenerator
from memory import MemoryManager


class RagPipeline:
    """
    Orchestrates the RAG workflow: retrieves context, augments prompt, and generates responses using an LLM.
    Optionally manages conversation memory for multi-turn dialogue.
    """

    def __init__(
        self,
        retriever: BaseVectorStore,
        generator: LLMGenerator,
        memory_manager: Optional[MemoryManager] = None,
    ):
        self.retriever = retriever
        self.generator = generator
        self.memory_manager = memory_manager

    def run(self, query):
        """
        Run the RAG pipeline for a user query.
        Retrieves context, prepares prompt, manages memory, and generates a response.
        """
        context = self.retriever.search_documents(query)

        prompt = self.prepare_prompt(query, context)

        if self.memory_manager:
            # Key is used to store from multiple sessions
            self.memory_manager.store("rag-test", "user", prompt)

            prompt = self.memory_manager.retrieve("rag-test")
        else:
            prompt = [{"role": "user", "content": prompt}]

        response = self.generator.generate(prompt)

        if self.memory_manager:
            # Key is used to store from multiple sessions
            self.memory_manager.store("rag-test", "system", response)

        return response

    def prepare_prompt(self, query, context):
        """
        Prepare the prompt for the LLM by combining the user query and retrieved context.
        """
        prompt_template = """You are an expert in answering user questions. You always understand user questions well, and then provide high-quality answers based on the information provided in the context.

If the provided context does not contain relevent information, just respond "I could not find the answer based on the context you provided."

User question: {}

Context:
{}
"""
        prompt = prompt_template.format(query, context)

        return prompt
