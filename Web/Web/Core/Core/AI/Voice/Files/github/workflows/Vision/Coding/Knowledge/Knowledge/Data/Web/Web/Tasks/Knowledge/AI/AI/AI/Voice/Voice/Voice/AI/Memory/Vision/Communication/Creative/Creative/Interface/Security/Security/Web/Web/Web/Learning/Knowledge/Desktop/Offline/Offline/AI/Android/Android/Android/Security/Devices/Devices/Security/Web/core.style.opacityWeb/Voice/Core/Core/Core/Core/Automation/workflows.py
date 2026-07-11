class Workflow:


    def create(self,name,steps):

        return {

            "name":name,

            "steps":steps

        }


    def run(self,workflow):

        return (
            "Running "
            + workflow["name"]
        )
