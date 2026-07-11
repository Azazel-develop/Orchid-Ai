import json
import os


class Knowledge:


    def __init__(self):

        self.file = (
            "Data/knowledge.json"
        )


        if not os.path.exists(
            self.file
        ):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    [],
                    f
                )



    def add(self,info):

        data=self.read()

        data.append(info)

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )



    def read(self):

        with open(
            self.file
        ) as f:

            return json.load(f)
