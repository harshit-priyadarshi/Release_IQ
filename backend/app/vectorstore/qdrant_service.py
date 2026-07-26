from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.config import (
    COLLECTION_NAME,
    QDRANT_HOST,
    QDRANT_PORT,
)


class QdrantService:

    def __init__(self):
        self.client = QdrantClient(
            host=QDRANT_HOST,
            port=QDRANT_PORT,
        )

    def create_collection(self, vector_size: int):

        collections = self.client.get_collections().collections

        collection_names = [c.name for c in collections]

        if COLLECTION_NAME in collection_names:
            print(f"Collection '{COLLECTION_NAME}' already exists.")
            return

        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{COLLECTION_NAME}' created successfully.")

    def upload_documents(self, chunks, embeddings):

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=chunk.metadata["chunk_id"],
                    vector=embedding,
                    payload={
                        "text": chunk.page_content,
                        **chunk.metadata
                    }
                )
            )

        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )

        print(f"Uploaded {len(points)} vectors.")

    def search(self, query_vector, limit=3):

        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=limit,
            with_payload=True
        )

        return results.points