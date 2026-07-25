from app.ingestion.loader import DocumentLoader
from app.ingestion.chunker import DocumentChunker


class IngestionPipeline:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()

    def run(self):
        documents = self.loader.load_all()
        chunks = self.chunker.split_documents(documents)

        return chunks