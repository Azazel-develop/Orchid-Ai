class Learning:


    def __init__(self):

        self.corrections=[]



    def learn(self,
              wrong,
              correct):

        self.corrections.append(
            {
            "wrong":wrong,
            "correct":correct
            }
        )



    def improve(self):

        return len(
            self.corrections
        )
