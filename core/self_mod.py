import os

class SelfModifier:
    def __init__(self):
        self.target_file = "core/engine.py"

    def apply_suggestion(self, suggestion):
        if "no change" in suggestion.lower():
            return

        print("\n[Self-Modification Suggestion]")
        print(suggestion)
        print("[Review manually before applying changes]\n")
        # Optionally: Write suggestion to a log or auto-apply