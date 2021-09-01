from domain.processor import Processor


class ProcessorNone(Processor):
    def __init__(self, file) -> None:
        super().__init__(file)
