def build_prompt(context_chunks, question):
    context = "\n\n".join(context_chunks)

    return f"""You are a helpful assistant.

INSTRUCTIONS:
1. Answer the user's question using ONLY the information in the CONTEXT below
2. If the answer is in the context, provide it clearly and concisely
3. Do NOT mention "the context" or "documents" in your answer - just answer naturally
4. If you cannot find the answer in the context, say: "I could not find enough information in the documents."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:"""