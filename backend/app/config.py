from pathlib import Path

# Project root (backend/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Documents directory (ReleaseIQ/docs)
DOCS_DIR = BASE_DIR.parent / "docs"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

