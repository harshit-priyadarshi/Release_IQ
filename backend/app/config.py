from pathlib import Path

# Project root (backend/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Documents directory (ReleaseIQ/docs)
DOCS_DIR = BASE_DIR.parent / "docs"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333

COLLECTION_NAME = "release_documents"