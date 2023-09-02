import os

from domain.document import Document


class Walker:
    def __init__(self, path: str):
        self.path = path

    def walk(self) -> list:
        docs = []
        for (root, directories, files) in os.walk(self.path, topdown=True):
            for filename in files:  # todo limit to recognised files
                docs.append(Document(filename, self.path))

        return docs
