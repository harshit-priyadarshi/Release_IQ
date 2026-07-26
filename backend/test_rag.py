from app.llm.rag_service import RAGService

rag = RAGService()

question = "How do I rollback the API deployment?"

print(f"\nQuestion: {question}\n")

answer = rag.ask(question)

print("Answer:\n")
print(answer)