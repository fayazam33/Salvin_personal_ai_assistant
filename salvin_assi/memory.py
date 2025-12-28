import json
import os

class Memory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def add(self, role, message):
        data = self.get_history()
        data.append({"role": role, "message": message})
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def get_history(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def clear(self):
        with open(self.file_path, "w") as f:
            json.dump([], f)
