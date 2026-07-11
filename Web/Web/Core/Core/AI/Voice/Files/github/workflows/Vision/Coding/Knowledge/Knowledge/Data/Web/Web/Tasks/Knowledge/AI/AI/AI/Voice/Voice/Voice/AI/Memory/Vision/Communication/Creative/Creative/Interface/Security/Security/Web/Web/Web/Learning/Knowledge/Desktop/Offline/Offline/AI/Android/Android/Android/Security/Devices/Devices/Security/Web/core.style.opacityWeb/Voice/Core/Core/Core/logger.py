import datetime


class Logger:


    def log(self,message):

        time=datetime.datetime.now()

        print(
            f"[{time}] {message}"
        )
