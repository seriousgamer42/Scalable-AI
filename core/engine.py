import json
from core.memory import MemoryManager
from core.self_mod import SelfModifier
from models.inference import LocalLLM

class AICore:
    def __init__(self, config):
        self.config = config
        self.memory = MemoryManager()
        self.llm = LocalLLM()
        self.self_mod = SelfModifier()

    def process_input(self, user_input):
        self.memory.log("input", user_input)

        context = self.memory.recall_recent(limit=5)
        full_prompt = "\n".join(context + [f"User: {user_input}", "AI:"])
        response = self.llm.generate(full_prompt)

        self.memory.log("response", response)
        return response

    def reflect_and_adapt(self):
        logs = self.memory.get_logs()
        suggestion = self.llm.generate_reflection(logs)
        self.self_mod.apply_suggestion(suggestion)