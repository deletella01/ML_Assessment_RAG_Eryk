from fastapi import FastAPI
from .retriever import retrieve
from .prompt import build_prompt
from .llm import generate_answer
from .schemas import ChatRequest, ChatResponse, Source

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    results = retrieve(req.question)

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    prompt = build_prompt(docs, req.question)
    answer = generate_answer(prompt)

    sources = [
        Source(source=m["source"], chunk_id=m["chunk_id"])
        for m in metas
    ]

    return ChatResponse(answer=answer, sources=sources)