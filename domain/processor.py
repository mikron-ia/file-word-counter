class Processor:
    def __init__(self, file_location) -> None:
        self.file_location = file_location
        self.file = self.load_file()
        self.data = self.unpack()

    @property
    def word_count(self):
        raise NotImplementedError

    def load_file(self):
        raise NotImplementedError

    def unpack(self):
        raise NotImplementedError
