class Processor:
    def __init__(self, file) -> None:
        self.file = file

    @property
    def word_count(self):
        raise NotImplementedError

    def unpack(self):
        raise NotImplementedError
