class LocalAI:


    def __init__(self):

        self.status = "ready"



    def generate(self, prompt):

        # Connection point for:
        # local GGUF models
        # llama.cpp
        # other offline engines


        response = (
            "Orchid AI received: "
            + prompt
        )


        return response
