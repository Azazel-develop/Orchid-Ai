import os


class Scanner:


    def scan_folder(self,path):

        results=[]


        for root,dirs,files in os.walk(path):

            for file in files:

                if file.endswith(
                    (".exe",".bat",".cmd")
                ):

                    results.append(
                        file
                    )


        return results
