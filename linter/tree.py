from typing import Iterator

from astroid.node_classes import NodeNG


class SyntaxTree:
    def __init__(self, root: NodeNG):
        """
        Constructor
        Parameters:
            root: root node of this tree
        """
        self._root = root

    def get_root(self) -> NodeNG:
        """Returns the root node"""
        return self._root

    @staticmethod
    def post_order_traversal(node: NodeNG) -> Iterator[NodeNG]:
        for child_node in node.get_children():
            yield from SyntaxTree.post_order_traversal(child_node)
        yield node

    @staticmethod
    def pre_order_traversal(node: NodeNG) -> Iterator[NodeNG]:
        yield node
        for child_node in node.get_children():
            yield from SyntaxTree.pre_order_traversal(child_node)

    def post_order(self) -> Iterator[NodeNG]:
        yield from self.post_order_traversal(self._root)

    def pre_order(self) -> Iterator[NodeNG]:
        yield from self.pre_order_traversal(self._root)
