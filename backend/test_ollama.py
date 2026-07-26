from app.llm.ollama_client import OllamaClient

client = OllamaClient()

response = client.generate(
    "In one sentence, explain what Kubernetes is."
)

print(response)