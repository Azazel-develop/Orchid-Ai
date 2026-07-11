import os


class CodingAgent:


    def create_code(
        self,
        filename,
        code
    ):

        os.makedirs(
            "Coding/projects",
            exist_ok=True
        )


        path = (
            "Coding/projects/"
            + filename
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(code)


        return (
            "Created code file: "
            + path
        )



    def explain(self, code):

        return (
            "Code explanation generated."
        )
