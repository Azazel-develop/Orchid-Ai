class LocalModel:


    def __init__(self):

        self.model="Orchid Local AI"



    def load(self):

        return (
            "Local model loaded."
        )



    def answer(self,prompt):

        return (
            "Orchid response: "
            + prompt
        )
