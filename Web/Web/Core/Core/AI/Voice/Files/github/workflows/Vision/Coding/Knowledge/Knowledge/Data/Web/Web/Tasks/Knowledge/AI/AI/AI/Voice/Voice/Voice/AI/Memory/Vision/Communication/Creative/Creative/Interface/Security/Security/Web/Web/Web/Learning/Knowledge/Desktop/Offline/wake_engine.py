class WakeEngine:


    def __init__(self):

        self.word = "hey orchid"
        self.active = True



    def detect(self, speech):

        if self.word in speech.lower():

            return True

        return False



    def activate(self):

        return "Orchid activated."
