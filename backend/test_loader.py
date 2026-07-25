from app.ingestion.loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_all()

print(f"Loaded {len(documents)} documents\n")

for doc in documents:
    print("=" * 50)
    print(doc.metadata)
    print()
    print(doc.page_content[:300])