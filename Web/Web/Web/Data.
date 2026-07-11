from AI.model import AIModel
from Core.memory import Memory
from Core.personality import Personality
from Core.planner import Planner


class OrchidBrain:


    def __init__(self):

        self.ai = AIModel()
        self.memory = Memory()
        self.personality = Personality()
        self.planner = Planner()



    def answer(self, user, message):

        self.memory.save(
            user,
            message
        )


        style = self.personality.check(
            message
        )


        if style:
            return style


        return self.ai.think(
            message
        )
