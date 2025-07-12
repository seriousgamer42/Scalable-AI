import json
import os
from datetime import datetime

class MemoryManager:
    def __init__(self, path="logs/memory.json"):
        self.path = path
        if not os.path.exists(path):
            with open(path, "w") as f:
                json.dump([], f)

    def log(self, kind, content):
        log_entry = {
            "time": datetime.now().isoformat(),
            "type": kind,
            "content": content
        }
        data = self.get_logs()
        data.append(log_entry)
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def recall_recent(self, limit=5):
        data = self.get_logs()
        return [f"{item['type'].capitalize()}: {item['content']}" for item in data[-limit:]]

    def get_logs(self):
        with open(self.path, "r") as f:
            return json.load(f)