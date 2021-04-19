class Document:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.file = self.__load_file(path)

    @property
    def type(self):
        raise NotImplementedError

    @property
    def word_count(self):
        raise NotImplementedError

    def __load_file(self, path):
        raise NotImplementedError
