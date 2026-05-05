# RAG Chatbot (FastAPI + Chroma + Ollama)

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that answers questions over a document corpus.

The system ingests `.txt` documents, indexes them using semantic embeddings, retrieves relevant context for a query, and generates grounded answers using a local LLM via Ollama.

---

## Architecture

User Query → Embedding → Retrieval (Chroma) → Context Injection → LLM (Ollama) → Answer

---

## Project Structure

```
Project

│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── ingest.py          # Data ingestion pipeline
│   ├── chunking.py        # Text splitting logic
│   ├── embeddings.py      # Embedding model wrapper
│   ├── vectordb.py        # Chroma setup
│   ├── retriever.py       # Retrieval logic
│   ├── llm.py             # Ollama interaction
│   ├── prompt.py          # Prompt template
│   └── schemas.py         # Request/response models
│
├── data/                  # Provided .txt files
├── chroma_db/             # Persistent vector store
├── requirements.txt
└── README.md
```
## Key Design Decisions

### 1. Embeddings
- Model: `all-MiniLM-L6-v2`

- Reason: lightweight, fast, strong baseline for semantic search
### 2. Chunking
- Size: 500 words

- Overlap: 100 words
- Reason: balance between context preservation and retrieval precision
### 3. Vector Store
- Chroma (persistent local storage)

- Reason: simple, no infrastructure required
### 4. LLM
- Ollama (`llama3`)

- Reason: local inference, open-source, easy integration

### 5. Grounding Strategy
- Answers restricted to retrieved context
- Explicit fallback if answer is not found
- Sources returned with each response

---

## How It Works

1. Documents are split into chunks
2. Chunks are embedded and stored in Chroma
3. Query is embedded at runtime
4. Top-k relevant chunks are retrieved
5. LLM generates answer using only retrieved context

---

## Setup Instructions

1. Clone the repository

2. Create a virtual environment (recommended)
On MacOS/Linux
- python -m venv venv
- source venv/bin/activate

On Windows:
venv\Scripts\activate

3. Install Python dependencies
pip install -r requirements.txt

4. Install Ollama

- macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh
- Windows
Download installer: https://ollama.com/download
Run the installer and follow the setup steps

5. Start the Ollama server
ollama serve

This starts the server at:
http://localhost:11434

6. Pull the LLM model
ollama pull llama3

Verify installation:
ollama list

7. Add your dataset

Place your .txt files inside:

/data

Example:

data/
  ai_policy.txt
  governance_framework.txt

8. Run data ingestion
python -m app.ingest

This step:
Reads all .txt files
Splits them into chunks
Generates embeddings
Stores them in chroma_db/

9. Start the API server
uvicorn app.main:app --reload

API base URL:

http://localhost:8000

API Usage

Endpoint: 
POST /chat

#### Test via Postman: POST/http://127.0.0.1:8000/chat

Request:
{
  "question": "What is AI governance?"
}

Response:
{
    "answer": "AI governance refers to the process of establishing rules, standards, and norms for the development, deployment, and use of artificial intelligence (AI) systems to ensure that they are safe, ethical, transparent, and beneficial to society. It involves the coordination of various stakeholders, including governments, private companies, research institutions, and civil society organizations, to promote responsible AI innovation and mitigate potential risks and negative consequences.",
    "sources": [
        {
            "source": "1144.txt",
            "chunk_id": 2
        },
        {
            "source": "1387.txt",
            "chunk_id": 9
        },
        {
            "source": "1076.txt",
            "chunk_id": 1
        },
        {
            "source": "307.txt",
            "chunk_id": 4
        },
        {
            "source": "35.txt",
            "chunk_id": 1
        }
    ]
}
---
