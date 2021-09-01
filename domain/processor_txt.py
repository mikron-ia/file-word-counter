from domain.processor import Processor


class ProcessorTxt(Processor):
    def __init__(self, file) -> None:
        super().__init__(file)

    @property
    def word_count(self):
        return len(self.data.split())

    def unpack(self):
        return self.file
