import os


def generate(name,data):

    os.makedirs(
        "Generated",
        exist_ok=True
    )


    with open(
        "Generated/"+name,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(data)


    return "File generated"
