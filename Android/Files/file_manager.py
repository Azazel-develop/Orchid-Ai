import os


def create_file(name, text):

    with open(name, "w", encoding="utf-8") as file:
        file.write(text)


    return "File created"


def read_file(name):

    with open(name, "r", encoding="utf-8") as file:
        return file.read()
