from typing import List

from Indexer.TreeStrategies import BaseNode, FileSystemNode
from Indexer.TreeWalkStrategies import OSWalkStrategy


class BaseTree:
    def __init__(self):
        super().__init__()
        self.__nodes: List[BaseNode] = []
        self.__root: BaseNode = None

    def set_root(self, p_root: BaseNode):
        self.__root = p_root

    def get_root(self) -> BaseNode:
        return self.__root

    def parse_from_dir(self, p_dir):
        root = FileSystemNode.FileSystemNode(p_dir)
        self.__root = OSWalkStrategy.OSWalkStrategy.traverse(p_dir, BaseTree.create_node, root)

    @staticmethod
    def create_node(p_name: str, p_parent: FileSystemNode) -> FileSystemNode:
        node = FileSystemNode.FileSystemNode(p_name)
        node.set_parent(p_parent)
        p_parent.add_child(node)
        return node






