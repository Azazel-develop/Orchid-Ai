class Messenger:


    def send_message(self, app, contact, message):

        allowed_apps = [
            "email",
            "messages",
            "discord"
        ]


        if app not in allowed_apps:

            return "Permission required."


        return (
            "Message prepared for "
            + contact
            + ": "
            + message
        )
