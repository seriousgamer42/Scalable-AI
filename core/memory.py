import json
import os
from datetime import datetime


class MemoryManager:
    def __init__(self, path="logs/memory.json", recall_limit=8):
        self.path = path
        self.recall_limit = recall_limit
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def log(self, kind, content):
        log_entry = {
            "time": datetime.now().isoformat(),
            "type": kind,
            "content": content,
        }
        data = self.get_logs()
        data.append(log_entry)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def recall_recent(self, limit=None):
        limit = self.recall_limit if limit is None else limit
        data = self.get_logs()
        return [
            f"{item['type'].capitalize()}: {item['content']}"
            for item in data[-limit:]
        ]

    def get_logs(self):
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)
