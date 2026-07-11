from AI.local_engine import LocalAI


class AIModel:

    def __init__(self):

        self.engine = LocalAI()


    def think(self, text):

        return self.engine.generate(text)
