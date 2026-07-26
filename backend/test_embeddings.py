from app.ingestion.pipeline import IngestionPipeline
from app.embeddings.embedder import EmbeddingService

pipeline = IngestionPipeline()
chunks = pipeline.run()

embedder = EmbeddingService()

embeddings = embedder.embed_documents(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")

print()

print("Embedding dimension:")

print(len(embeddings[0]))