# RAG CyberSec LLM

A Retrieval-Augmented Generation (RAG) pipeline for cybersecurity question answering using large language models (LLMs) and vector search over a custom dataset.

## Features

- Loads and preprocesses cybersecurity articles from Excel datasets
- Splits and embeds documents using Sentence Transformers
- Stores and retrieves document embeddings with ChromaDB
- Generates answers using Google Gemma LLM (quantized, via HuggingFace Transformers)
- Optional memory management for chat history

## Installation

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd rag-cybersec-llm
   ```

2. **Install Python dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

   Ensure you have Python 3.8+ and a CUDA-capable GPU for best performance.

3. **Prepare the dataset:**
   - Place your Excel file (e.g., `TheHackerNews_Dataset.xlsx`) in `data/raw/`.

## Usage

Run the main script:

```sh
python main.py
```

This will:

- Load and preprocess the dataset
- Index documents into ChromaDB
- Run a sample RAG pipeline query using the Gemma LLM

## Hugging Face Token

To use the Gemma LLM, you need a Hugging Face access token. Set your token as an environment variable before running the script:

On Linux/macOS:

```sh
export HF_TOKEN=your_hf_token_here
```

On Windows (PowerShell):

```powershell
$env:HF_TOKEN="your_hf_token_here"
```

Alternatively, you will be prompted to log in interactively the first time you run the script.

## Project Structure

- `main.py` — Entry point
- `preprocessors/` — Data loading and splitting
- `embeddings/` — Vector store logic (ChromaDB)
- `generators/` — LLM wrapper (Gemma)
- `memory/` — Optional chat memory management
- `pipelines/` — RAG pipeline logic
- `utils/` — Shared types

## Requirements

- Python 3.8+
- CUDA-capable GPU (for LLM inference)
- See `requirements.txt` for all dependencies

## License

MIT License
# rag-pipeline-test
