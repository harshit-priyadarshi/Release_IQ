from app.embeddings.embedder import EmbeddingService
from app.vectorstore.qdrant_service import QdrantService

embedder = EmbeddingService()

vector = embedder.embed_text("Hello ReleaseIQ")

qdrant = QdrantService()

qdrant.create_collection(len(vector))