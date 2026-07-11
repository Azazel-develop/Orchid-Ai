"""
Orchid AI - Core Engine
Version 0.1

A free personal AI assistant foundation.
"""

import datetime
import os
import platform


class Orchid:
    def __init__(self):
        self.name = "Orchid"
        self.memory = []

    def speak(self, text):
        print(f"Orchid: {text}")

    def remember(self, text):
        self.memory.append(text)

    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M")

    def system_info(self):
        return platform.system()

    def create_file(self, filename, content):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            return f"Created file {filename}"
        except Exception as e:
            return str(e)

    def command(self, user_input):

        command = user_input.lower()

        if "hello" in command:
            return "Hello. I am Orchid."

        if "time" in command:
            return f"The time is {self.get_time()}"

        if "remember" in command:
            note = user_input.replace("remember", "")
            self.remember(note)
            return "I saved that memory."

        if "system" in command:
            return f"You are running {self.system_info()}"

        if "create file" in command:
            return self.create_file(
                "orchid_file.txt",
                "Created by Orchid AI"
            )

        return "I don't know that command yet."


orchid = Orchid()

orchid.speak("Online. Ready.")

while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit"]:
        orchid.speak("Goodbye.")
        break

    answer = orchid.command(user)
    orchid.speak(answer)
