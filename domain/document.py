from domain.processor_odt import ProcessorOdt
from domain.processor_docx import ProcessorDocx
from domain.processor_txt import ProcessorTxt


class Document:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.file = path  # self.__load_file(path)
        self.processor = self.__get_processor()

    @property
    def type(self):
        raise NotImplementedError

    @property
    def words(self):
        return self.processor.word_count

    def __load_file(self, path):
        raise NotImplementedError

    def __get_processor(self):
        return {
            'docx': ProcessorDocx,
            'odt': ProcessorOdt,
            'txt': ProcessorTxt,
        }.get(self.type)(self.file)
