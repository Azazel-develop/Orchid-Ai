class AgentManager:


    def choose(self,task):

        if "code" in task:

            return "Coding Agent"


        if "story" in task:

            return "Creative Agent"


        return "General Orchid Agent"
