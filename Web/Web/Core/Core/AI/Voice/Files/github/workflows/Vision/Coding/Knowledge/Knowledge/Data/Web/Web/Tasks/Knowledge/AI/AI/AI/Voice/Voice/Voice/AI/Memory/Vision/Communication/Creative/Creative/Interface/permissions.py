class PermissionManager:


    def request(self, action):

        print(
            "ORCHID REQUEST:"
        )

        print(action)

        answer=input(
            "Allow? yes/no: "
        )


        return answer.lower()=="yes"
