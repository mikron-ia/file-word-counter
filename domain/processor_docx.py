from functools import reduce

import docx

from domain.processor import Processor


class ProcessorDocx(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)

    @property
    def word_count(self):
        return reduce(
            lambda counter, row: counter + len(row.text.split()),
            self.content.paragraphs,
            0
        )

    def load_content_from_file(self):
        return docx.Document(self.file_location)
