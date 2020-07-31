from __future__ import annotations

from typing import List


class BaseNode:
    def __init__(self):
        self.__parent: BaseNode = None
        self.__children: List[BaseNode] = []
        self.__data = None

    def set_parent(self, p_parent: BaseNode) -> None:
        self.__parent = p_parent
        # p_parent.add_child(self)

    def get_parent(self) -> BaseNode:
        return self.__parent

    def set_data(self, p_data: List[any]):
        self.__data = p_data

    def get_data(self) -> List[any]:
        return self.__data

    def add_child(self, p_child: BaseNode) -> None:
        self.__children.append(p_child)
        # p_child.set_parent(self)

    def get_children(self) -> List[BaseNode]:
        return self.__children

    def delete_child(self, p_child: BaseNode) -> None:
        self.__children.remove(p_child)
        p_child.set_parent(None)

