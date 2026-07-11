class Personality:


    def reply(self,text):


        if "joke" in text.lower():

            return (
            "Very funny. "
            "You asked an AI for humor. "
            "Bold choice."
            )


        if "are you smart" in text.lower():

            return (
            "Smart enough to help. "
            Still waiting for you to stop testing me."
            )


        return None
