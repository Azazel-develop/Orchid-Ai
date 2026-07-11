class SpeechEngine:


    def __init__(self):

        self.voice = "Orchid"



    def speak(self,text):

        print(
            "🔊 Orchid:",
            text
        )


    def set_voice(self,name):

        self.voice=name
