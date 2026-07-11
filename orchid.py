from memory import Memory
from voice import Voice
import datetime


class Orchid:

    def __init__(self):

        self.name = "Orchid"
        self.memory = Memory()
        self.voice = Voice()


    def process(self, command):

        command = command.lower()


        if "hello" in command:
            return "Hello. I am Orchid."


        if "time" in command:

            return datetime.datetime.now().strftime(
                "The time is %H:%M"
            )


        if "remember" in command:

            note = command.replace(
                "remember",
                ""
            )

            self.memory.save(note)

            return "Memory saved."


        if "show memory" in command:

            memories = self.memory.read()

            return str(memories)


        if "clear memory" in command:

            self.memory.clear()

            return "Memory cleared."


        return "Command not learned yet."



orchid = Orchid()

orchid.voice.speak(
    "Orchid activated."
)


while True:

    command = orchid.voice.listen()


    if command.lower() == "exit":
        break


    response = orchid.process(command)

    orchid.voice.speak(response)
