from domain.processor import Processor


class ProcessorOdt(Processor):
    def __init__(self, file_location) -> None:
        super().__init__(file_location)
