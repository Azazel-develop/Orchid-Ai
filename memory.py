import json
import os


class Memory:

    def __init__(self):
        self.file = "memory.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)


    def save(self, information):

        with open(self.file, "r") as f:
            data = json.load(f)

        data.append(information)

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)


    def read(self):

        with open(self.file, "r") as f:
            return json.load(f)


    def clear(self):

        with open(self.file, "w") as f:
            json.dump([], f)
