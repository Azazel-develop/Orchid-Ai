import shutil


class Backup:


    def create(self):

        shutil.make_archive(
            "Orchid_Backup",
            "zip",
            "Data"
        )

        return (
            "Backup created."
        )
