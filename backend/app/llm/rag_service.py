from app.retrieval.retriever import Retriever
from app.llm.prompt_builder import PromptBuilder
from app.llm.ollama_client import OllamaClient


class RAGService:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = OllamaClient()

    def ask(self, question: str):

        retrieved_chunks = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build_prompt(
            question,
            retrieved_chunks,
        )

        answer = self.llm.generate(prompt)

        return answer