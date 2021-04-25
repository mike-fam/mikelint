from linter.tree import SyntaxTree


class Analyser:
    def __init__(self, tree: SyntaxTree):
        """

        Args:
            tree:
        """
        self._tree = tree
        # TODO: manage tree
        #   manage rules, maybe config file
