import os
import shutil


class Quarantine:


    def move(self,file):

        os.makedirs(
            "Quarantine",
            exist_ok=True
        )


        shutil.move(
            file,
            "Quarantine/"
        )


        return (
            "File moved to quarantine."
        )
