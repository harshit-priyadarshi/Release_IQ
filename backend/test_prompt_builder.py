from app.retrieval.retriever import Retriever
from app.llm.prompt_builder import PromptBuilder

retriever = Retriever()
builder = PromptBuilder()

results = retriever.retrieve(
    "How do I rollback the API deployment?"
)

prompt = builder.build_prompt(
    "How do I rollback the API deployment?",
    results
)

print(prompt)