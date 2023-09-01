import os


class Walker:
    def __init__(self, path: str):
        self.path = path

    def walk(self):
        for (root, directories, files) in os.walk(self.path, topdown=True):
            print(files)
            # todo for useful types of file: check, open, count
