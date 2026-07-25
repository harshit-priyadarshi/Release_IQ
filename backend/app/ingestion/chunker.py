from uuid import uuid4

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_SIZE, CHUNK_OVERLAP


class DocumentChunker:

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):

        chunks = self.splitter.split_documents(documents)

        for index, chunk in enumerate(chunks):

            chunk.metadata["chunk_id"] = str(uuid4())
            chunk.metadata["chunk_index"] = index
            chunk.metadata["char_count"] = len(chunk.page_content)
            chunk.metadata["word_count"] = len(chunk.page_content.split())

            source = chunk.metadata["source"]

            if source.endswith(".pdf"):
                chunk.metadata["document_type"] = "pdf"
            elif source.endswith(".md"):
                chunk.metadata["document_type"] = "markdown"
            else:
                chunk.metadata["document_type"] = "unknown"

        return chunks