class Debugger:


    def check(self, code):

        if "error" in code.lower():

            return (
                "Possible error found."
            )


        return (
            "No obvious problems detected."
        )
