from app.embeddings.embedder import EmbeddingService
from app.vectorstore.qdrant_service import QdrantService


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingService()

        self.vectorstore = QdrantService()

    def retrieve(self, query: str, top_k: int = 3):

        print(f"Searching for: {query}")

        query_embedding = self.embedder.embed_text(query)

        results = self.vectorstore.search(
            query_embedding,
            limit=top_k
        )

        return results