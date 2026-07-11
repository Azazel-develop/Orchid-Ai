class Voice:

    def __init__(self):
        self.active = True


    def listen(self):

        # Temporary browser/testing input
        # Will become microphone input later

        command = input("Voice: ")
        return command


    def speak(self, text):

        # Temporary output
        # Will become real speech later

        print("Orchid Voice:", text)
