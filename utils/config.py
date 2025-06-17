"""
Configuration module for RAG pipeline.
Define global settings, paths, and environment variables here.
"""
import os

# Example: Path to data directory
data_dir = os.getenv("DATA_DIR", "./data/")

# Example: Model name for LLM
default_llm_model = os.getenv("LLM_MODEL", "google/gemma-1.1-7b-it")

# Example: ChromaDB persistent path
chroma_persist_path = os.getenv("CHROMA_PATH", "./chroma_db/")
