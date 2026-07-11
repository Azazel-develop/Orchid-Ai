class Search:


    def find(
        self,
        database,
        word
    ):

        results=[]


        for item in database:

            if word.lower() in str(item).lower():

                results.append(item)


        return results
