from app.ingestion.pipeline import IngestionPipeline
from app.embeddings.embedder import EmbeddingService
from app.vectorstore.qdrant_service import QdrantService


class DocumentIndexer:

    def __init__(self):

        self.pipeline = IngestionPipeline()

        self.embedder = EmbeddingService()

        self.vectorstore = QdrantService()

    def index_documents(self):

        print("Loading documents...")

        chunks = self.pipeline.run()

        print(f"{len(chunks)} chunks created.")

        print("Generating embeddings...")

        embeddings = self.embedder.embed_documents(chunks)

        print("Creating collection...")

        self.vectorstore.create_collection(
            len(embeddings[0])
        )

        print("Uploading vectors...")

        self.vectorstore.upload_documents(
            chunks,
            embeddings
        )

        print("Indexing completed successfully!")