class Personality:


    def check(self,message):


        text=message.lower()


        if "joke" in text:

            return (
            "I would tell you a joke, "
            "but your last command was already "
            "pretty funny."
            )


        if "who is better" in text:

            return (
            "Obviously Orchid. "
            "I am the one answering."
            )


        return None
