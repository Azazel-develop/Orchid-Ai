from Core.config import Config
from Core.logger import Logger


class OrchidCore:


    def __init__(self):

        self.config = Config()
        self.logger = Logger()



    def start(self):

        self.logger.log(
            "Orchid starting..."
        )


        print(
            """
            🌸 ORCHID AI

            Core Online
            Systems Ready
            """
        )


        self.load_modules()



    def load_modules(self):

        modules = [

            "AI",
            "Voice",
            "Memory",
            "Security",
            "Devices",
            "Knowledge"

        ]


        for module in modules:

            self.logger.log(
                module + " loaded"
            )



        print(
            "All systems initialized."
        )
