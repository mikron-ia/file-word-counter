from functools import reduce

from odf import text, teletype
from odf.opendocument import load as load_odt

from domain.processor import Processor


class ProcessorOdt(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)

    @property
    def word_count(self):
        rows = self.content.getElementsByType(text.P)
        return reduce(lambda counter, row: counter + len(teletype.extractText(row).split()), rows, 0)

    def load_content_from_file(self):
        return load_odt(self.file_location)
