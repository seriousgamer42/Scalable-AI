import requests


class LocalLLM:
    """OpenAI-compatible client for a local LM Studio server."""

    def __init__(self, config=None):
        config = config or {}
        llm_config = config.get("llm", {})
        self.base_url = llm_config.get("base_url", "http://127.0.0.1:1234/v1").rstrip("/")
        self.model = llm_config.get("model", "local-model")
        self.api_key = llm_config.get("api_key", "lm-studio")
        self.temperature = llm_config.get("temperature", 0.7)
        self.max_tokens = llm_config.get("max_tokens", 1024)
        self.timeout = llm_config.get("timeout", 120)

    def generate(self, prompt):
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            },
            timeout=self.timeout,
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    def generate_reflection(self, logs):
        combined = "\n".join(
            f"{item['type']}: {item['content']}" for item in logs[-5:]
        )
        prompt = (
            "Based on this interaction history, how should the AI improve?\n\n"
            f"{combined}\n\nReflection:"
        )
        return self.generate(prompt)
