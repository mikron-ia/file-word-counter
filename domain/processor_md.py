from domain.processor import Processor


class ProcessorMd(Processor):
    def __init__(self, file) -> None:
        super().__init__(file)

    @property
    def word_count(self):
        purged_text = self.data.replace('#', '')
        return len(purged_text.split())

    def unpack(self):
        return self.file
