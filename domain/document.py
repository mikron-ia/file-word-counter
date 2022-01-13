from os import path

from domain.processor_docx import ProcessorDocx
from domain.processor_md import ProcessorMd
from domain.processor_none import ProcessorNone
from domain.processor_odt import ProcessorOdt
from domain.processor_txt import ProcessorTxt


class Document:
    def __init__(self, file_name, file_path):
        self.file_name = file_name
        self.file_path = file_path
        self.processor_class = self.__get_processor()
        self.processor = self.__load_file_to_processor()

    @property
    def type(self):  # todo Verify the format
        extension = path.splitext(self.file_name)[-1]

        if not extension:
            return None

        return extension.replace('.', '')

    @property
    def words(self):
        return self.processor.word_count

    def __get_processor(self):
        return {
            'docx': ProcessorDocx,
            'odt': ProcessorOdt,
            'txt': ProcessorTxt,
            'md': ProcessorMd,
        }.get(self.type, ProcessorNone)

    def __load_file_to_processor(self):
        return self.processor_class(self.file_path + "/" + self.file_name)
