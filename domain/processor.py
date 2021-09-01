from domain.errors import *


class Processor:
    def __init__(self, file) -> None:
        self.file = file
        self.data = self.unpack()

    @property
    def word_count(self):
        raise UnrecognizedType

    def unpack(self):
        raise UnrecognizedType
