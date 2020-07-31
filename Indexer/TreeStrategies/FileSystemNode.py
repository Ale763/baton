from Indexer.TreeStrategies.BaseNode import BaseNode


class FileSystemNode(BaseNode):
    def __init__(self, p_name):
        super().__init__()
        self.__name = p_name


