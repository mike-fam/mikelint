from linter.analysers.analyser import Analyser, register_check
from astroid import Global, Const


class ScopeAnalyser(Analyser):
    # TODO: Maybe this is too strict?
    MAGIC_WHITELIST = ["", 0, 1, -1, " ", 100, True, False, None, "__main__"]

    @register_check("Globals used on line {}:\n\t{}")
    def check_globals(self):
        """Checks if code has any global variables"""
        # lineno, line
        result: list[tuple[int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, Global):
                continue
            result.append((node.lineno, self.get_line(node.lineno)))
        return result

    @register_check("Magic values used on line {}:\n\t{}")
    def check_constants_used(self):
        """Check if any value that could have been used as constants"""
        # lineno, line
        result: list[tuple[int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, Const):
                continue
            if node.value in self.MAGIC_WHITELIST:
                continue
            result.append((node.lineno, self.get_line(node.lineno)))
        return result

