from ollama import Client


class OllamaClient:

    def __init__(
        self,
        model: str = "llama3.2:3b",
        host: str = "http://localhost:11434",
    ):
        self.model = model
        self.client = Client(host=host)

    def generate(self, prompt: str) -> str:

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.message.content