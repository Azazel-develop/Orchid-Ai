class DocumentAI:


    def analyze(self,text):

        words=len(
            text.split()
        )


        return {

            "length":words,

            "summary":
            text[:200]

        }
