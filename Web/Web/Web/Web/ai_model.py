class AIModel:


    def __init__(self):

        self.name = "Orchid Brain"



    def think(self, message):

        # Placeholder for local AI model
        # Later connect:
        # llama.cpp
        # Ollama
        # other local models

        responses = {

            "hello":
            "Hello. I was waiting for you.",

            "who are you":
            "I am Orchid, your personal AI assistant."

        }


        for key in responses:

            if key in message.lower():

                return responses[key]


        return (
            "I understand your request. "
            "My advanced model connection "
            "is being upgraded."
        )
