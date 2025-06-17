# RAG CyberSec LLM

A Retrieval-Augmented Generation (RAG) pipeline for cybersecurity question answering using large language models (LLMs) and vector search over a custom dataset.

---

## Architecture Overview

This project is organized as a modular, multi-layered pipeline:

- **Preprocessing**: Loads and cleans raw cybersecurity articles from Excel datasets.
- **Retriever**: Indexes and searches documents using ChromaDB and Sentence Transformers.
- **LLM Integration**: Wraps a large language model (Google Gemma) for response generation.
- **Conversation Memory**: (Optional) Stores and retrieves previous conversation history for context-aware responses.
- **Inference Pipeline**: Orchestrates the retrieval, prompt augmentation, and LLM call.
- **Utils & Config**: Shared types, configuration, and utility functions.

### Architecture Diagram

```
[User Query]
     |
     v
[Conversation Memory] <----> [Previous Conversations]
     |
     v
[Retriever] <-----> [Indexed Cybersecurity Docs]
     |
     v
[LLM Integration]
     |
     v
[Response]
```

---

## Features

- Loads and preprocesses cybersecurity articles from Excel datasets
- Splits and embeds documents using Sentence Transformers
- Stores and retrieves document embeddings with ChromaDB
- Generates answers using Google Gemma LLM (quantized, via HuggingFace Transformers)
- Optional memory management for chat history

---

## Project Structure

```
rag-pipeline-test/
├── README.md
├── requirements.txt
├── data/                # Raw and processed documents
│   └── raw/
├── embeddings/          # Vector store logic (ChromaDB)
├── generators/          # LLM wrapper (Gemma)
├── memory/              # Optional chat memory management
├── pipelines/           # RAG pipeline logic
├── preprocessors/       # Data loading and splitting
├── utils/               # Shared types, config, etc.
├── tests/               # Integration and unit tests
```

---

## Installation

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd rag-pipeline-test
   ```

2. **Install Python dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

   Ensure you have Python 3.8+ and a CUDA-capable GPU for best performance.

3. **Prepare the dataset:**
   - Place your Excel file (e.g., `TheHackerNews_Dataset.xlsx`) in `data/raw/`.

---

## Usage

Run the main script:

```sh
python main.py
```

This will:
- Load and preprocess the dataset
- Index documents into ChromaDB
- Run a sample RAG pipeline query using the Gemma LLM

---

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

---

## How the Pipeline Works

1. **Preprocessing**: Loads and splits articles from Excel into manageable chunks.
2. **Embedding & Indexing**: Chunks are embedded and stored in ChromaDB for fast retrieval.
3. **Retrieval**: On user query, relevant chunks are retrieved from the vector store.
4. **Prompt Augmentation**: Retrieved context and conversation history are combined into a prompt.
5. **LLM Generation**: The prompt is sent to the Gemma LLM for answer generation.
6. **Memory Management**: (Optional) Stores conversation turns for context-aware dialogue.

---

## Design Decisions

- **Why RAG + LLM?**
  - RAG enables the LLM to access up-to-date, factual information, critical for cybersecurity.
  - Conversation memory allows for coherent, multi-turn dialogues.
  - Fine-tuning on cybersecurity data (if available) can further improve relevance and accuracy.
- **Why ChromaDB?**
  - Efficient, persistent vector search for document retrieval.
- **Why Google Gemma?**
  - State-of-the-art LLM with quantization support for efficient inference.

---

## Configuration

- Global settings (e.g., data paths, model names) can be managed in `utils/config.py`.
- Environment variables are supported for easy overrides.

---

## Requirements

- Python 3.8+
- CUDA-capable GPU (for LLM inference)
- See `requirements.txt` for all dependencies

---

## License

MIT License

---

## Further Reading

- [Huggingface Transformers](https://huggingface.co/transformers/)
- [ChromaDB](https://www.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)

---

## Evaluation with DeepEval and Gemini

Before running the evaluation script, set up Gemini as the LLM for DeepEval:

```sh
deepeval set-gemini --model-name="gemini-2.0-flash-001" --google-api-key=$GOOGLE_API_KEY
```

Then run the evaluation script:

```sh
python evaluate_rag_pentesting_eval.py
```

This will evaluate your RAG pipeline using the HuggingFace pentesting-eval dataset and DeepEval metrics.
