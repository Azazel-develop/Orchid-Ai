import os


def create_file(filename, content):

    folder = "Generated"

    os.makedirs(
        folder,
        exist_ok=True
    )


    path = os.path.join(
        folder,
        filename
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)


    return (
        "Created file: "
        + path
    )
