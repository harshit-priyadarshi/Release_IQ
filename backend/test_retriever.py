from app.retrieval.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "How do I rollback the API deployment?"
)

print()

print(f"Retrieved {len(results)} chunks\n")

for i, result in enumerate(results, start=1):

    print("=" * 60)

    print(f"Result {i}")

    print(f"Score: {result.score:.4f}")

    print()

    payload = result.payload

    print("Source:", payload["source"])

    print()

    print(payload["text"])