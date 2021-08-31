from domain.processor import Processor


class ProcessorDocx(Processor):
    def __init__(self, file) -> None:
        super().__init__(file)

    @property
    def word_count(self):
        raise NotImplementedError  # todo

    def unpack(self):
        raise NotImplementedError  # todo
