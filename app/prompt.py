def build_prompt(context_chunks, question):
    context = "\n\n".join(context_chunks)

    return f"""
You are a helpful assistant.

Answer ONLY using the context below.
If the answer is not in the context, say:
"I could not find enough information in the documents."

Context:
{context}

Question:
{question}

Answer:
"""