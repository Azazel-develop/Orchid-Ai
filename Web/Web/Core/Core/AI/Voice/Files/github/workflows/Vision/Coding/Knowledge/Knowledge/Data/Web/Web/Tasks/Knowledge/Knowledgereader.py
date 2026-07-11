import os


def read_text_file(path):

    if not os.path.exists(path):

        return "File not found"


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()
