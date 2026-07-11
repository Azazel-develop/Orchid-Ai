class PermissionManager:


    def ask(self,action):

        print(
            "Orchid wants permission:"
        )

        print(action)


        answer=input(
            "Allow? "
        )


        return answer.lower()=="yes"
