import os

from Indexer.TreeStrategies import FileSystemNode, BaseNode


class OSWalkStrategy:
    @staticmethod
    def traverse(p_dir: str, create_node, root: FileSystemNode.FileSystemNode=None) -> FileSystemNode.FileSystemNode:
        # root = FileSystemNode.FileSystemNode(p_dir)
        contents = os.listdir(p_dir)
        for item in contents:
            path_name = os.path.join(p_dir, item)
            child = create_node(path_name, root)
            # child: FileSystemNode = FileSystemNode.FileSystemNode(path_name)
            # root.add_child(child)
            if os.path.isdir(path_name):
                OSWalkStrategy.traverse(p_dir + "\\" + item,create_node, child)
        return root

    @staticmethod
    def print_traverse(p_dir: str, p_depth: int = 0) -> None:
        contents = os.listdir(p_dir)
        for item in contents:
            path_name = os.path.join(p_dir, item)
            print("\t" * p_depth + item)
            if os.path.isdir(path_name):
                OSWalkStrategy.traverse(p_dir + "\\" + item, p_depth + 1)
