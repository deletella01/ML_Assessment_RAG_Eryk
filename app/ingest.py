
import os

def ingest():
    from .chunking import chunk_text
    from .vectordb import collection

    DATA_DIR = "./data/fulltext"
    all_chunks = []
    metadatas = []
    ids = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            path = os.path.join(DATA_DIR, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            chunks = chunk_text(text)

            for i, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                metadatas.append({"source": file, "chunk_id": i})
                ids.append(f"{file}_{i}")

    collection.add(
        documents=all_chunks,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Ingestion complete: {len(all_chunks)} chunks from {len([f for f in os.listdir(DATA_DIR) if f.endswith('.txt')])} files")

if __name__ == "__main__":
    ingest()
