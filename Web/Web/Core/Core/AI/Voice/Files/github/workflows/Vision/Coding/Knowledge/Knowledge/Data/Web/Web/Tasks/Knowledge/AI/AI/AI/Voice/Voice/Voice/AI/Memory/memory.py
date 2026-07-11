import json
import os


class Memory:


    def __init__(self):

        self.file="Memory/database.json"


        if not os.path.exists(self.file):

            with open(self.file,"w") as f:

                json.dump({},f)



    def save(self,user,data):

        with open(self.file) as f:

            memory=json.load(f)


        if user not in memory:

            memory[user]=[]


        memory[user].append(data)


        with open(self.file,"w") as f:

            json.dump(
                memory,
                f,
                indent=4
            )



    def get(self,user):

        with open(self.file) as f:

            memory=json.load(f)


        return memory.get(user,[])
