from charset_normalizer import from_path

from domain.processor import Processor


class ProcessorTxt(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)

    @property
    def word_count(self):
        return len(self.content.split())

    def load_content_from_file(self):
        return str(from_path(self.file_location).best())
