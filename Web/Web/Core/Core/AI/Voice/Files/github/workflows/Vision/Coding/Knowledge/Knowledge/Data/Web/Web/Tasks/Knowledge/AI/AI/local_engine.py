class LocalAI:

    def __init__(self):
        self.model_name = "Orchid Local Model"


    def generate(self, prompt):

        # Connection point for local models
        # Example:
        # llama.cpp
        # GGUF models

        return (
            "Orchid processed your request: "
            + prompt
        )
