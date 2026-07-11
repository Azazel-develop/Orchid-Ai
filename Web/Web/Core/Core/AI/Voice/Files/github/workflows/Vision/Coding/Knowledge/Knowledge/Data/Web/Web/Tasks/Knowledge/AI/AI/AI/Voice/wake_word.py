class WakeWord:


    def __init__(self):

        self.word = "hey orchid"



    def detect(self, text):

        if self.word in text.lower():

            return True


        return False
