from domain.processor import Processor


class ProcessorTxt(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)

    @property
    def word_count(self):
        return len(self.content.split())

    def load_file(self):
        file = open(self.file_location, "r")
        return file.read()
