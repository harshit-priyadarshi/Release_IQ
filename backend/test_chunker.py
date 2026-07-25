from app.ingestion.pipeline import IngestionPipeline

pipeline = IngestionPipeline()

chunks = pipeline.run()

print(f"\nTotal Chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks):

    print("=" * 60)

    print(f"Chunk {i}")

    print(chunk.metadata)

    print()

    print(chunk.page_content)

    print()