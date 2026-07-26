class PromptBuilder:

    SYSTEM_PROMPT = """
You are ReleaseIQ, an AI assistant for release management.

Use ONLY the provided context to answer the user's question.

Rules:
- If the answer is not in the context, say:
  "I couldn't find that information in the documentation."
- Do not make up information.
- Keep answers concise.
- Mention the relevant source document(s) if possible.
"""

    def build_prompt(self, query: str, retrieved_chunks):

        context = ""

        for i, chunk in enumerate(retrieved_chunks, start=1):
            context += (
                f"\n===== Document {i} =====\n"
                f"Source: {chunk.payload['source']}\n\n"
                f"{chunk.payload['text']}\n"
            )

        prompt = f"""
{self.SYSTEM_PROMPT}

Context:
{context}

Question:
{query}

Answer:
"""

        return prompt