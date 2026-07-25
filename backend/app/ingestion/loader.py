from pathlib import Path
from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader,
)

from app.config import DOCS_DIR


class DocumentLoader:

    def load_markdown(self):
        loader = DirectoryLoader(
            DOCS_DIR,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
        )

        return loader.load()

    def load_pdf(self):
        loader = DirectoryLoader(
            DOCS_DIR,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
        )

        return loader.load()

    def load_all(self):

        documents = []

        documents.extend(self.load_markdown())
        documents.extend(self.load_pdf())

        # Normalize metadata
        for index, doc in enumerate(documents):
            source = Path(doc.metadata.get("source", "")).name
            doc.metadata["source"] = source
            doc.metadata["doc_id"] = f"doc_{index}"

        return documents