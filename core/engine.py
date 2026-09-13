from core.memory import MemoryManager
from core.self_mod import SelfModifier
from models.interference import LocalLLM


class AICore:
    def __init__(self, config):
        self.config = config
        memory_config = config.get("memory", {})
        self.memory = MemoryManager(
            path=memory_config.get("path", "logs/memory.json"),
            recall_limit=memory_config.get("recall_limit", 8),
        )
        self.llm = LocalLLM(config)
        self.self_mod = SelfModifier()
        self.reflection_enabled = config.get("reflection", {}).get("enabled", True)

    def process_input(self, user_input):
        self.memory.log("input", user_input)

        context = self.memory.recall_recent()
        full_prompt = "\n".join(context + [f"User: {user_input}", "AI:"])
        response = self.llm.generate(full_prompt)

        self.memory.log("response", response)
        return response

    def reflect_and_adapt(self):
        if not self.reflection_enabled:
            return

        logs = self.memory.get_logs()
        suggestion = self.llm.generate_reflection(logs)
        self.memory.log("reflection", suggestion)
        self.self_mod.apply_suggestion(suggestion)
