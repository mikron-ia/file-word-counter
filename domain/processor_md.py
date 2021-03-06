from domain.processor import Processor


class ProcessorMd(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)

    @property
    def word_count(self):
        purged_text = self.content.replace('#', '')
        return len(purged_text.split())

    def load_content_from_file(self):
        file = open(self.file_location, "r")
        return file.read()
