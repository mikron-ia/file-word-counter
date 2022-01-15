class Processor:
    def __init__(self, file_location) -> None:
        self.file_location = file_location
        self.content = self.load_file()

    @property
    def word_count(self):
        raise NotImplementedError

    def load_file(self):
        raise NotImplementedError
