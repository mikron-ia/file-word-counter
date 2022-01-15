from domain.errors import *
from domain.processor import Processor


class ProcessorNone(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)

    @property
    def word_count(self):
        raise UnrecognizedType

    def load_file(self):
        raise UnrecognizedType
