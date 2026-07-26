from sentence_transformers import SentenceTransformer

from app.config import EMBEDDING_MODEL


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed_text(self, text: str):

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_documents(self, chunks):

        texts = [chunk.page_content for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()