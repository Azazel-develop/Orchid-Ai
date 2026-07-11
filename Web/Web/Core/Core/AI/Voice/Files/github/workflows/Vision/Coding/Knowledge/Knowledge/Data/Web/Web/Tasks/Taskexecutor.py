class TaskExecutor:


    def run(self, task):

        allowed = [
            "create_file",
            "save_note",
            "search"
        ]


        if task in allowed:

            return "Task executed"


        return "Permission required"
