"""
Analyse scope violations
"""
from astroid import Global, Const

from .analyser import Analyser, register_check


class ScopeAnalyser(Analyser):
    """Analyser checking for scope violations"""
    MAGIC_WHITELIST = [0, 1, -1, 100]

    @register_check("{}:{}: Globals used:\n\t{}")
    def check_globals(self):
        """Checks if code has any global variables"""
        # lineno, line
        result: list[tuple[str, int, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, Global):
                    continue
                result.append((filename, node.lineno,
                               self.get_line(filename, node.lineno)))
        return result

    @register_check("{}:{}: Magic number used\n\t{}")
    def check_magic_numbers_used(self):
        """Check if any magic number has been used """
        # lineno, line
        result: list[tuple[str, int, str]] = []
        checked_lines = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, Const):
                    continue
                if node.value in self.MAGIC_WHITELIST:
                    continue
                if not isinstance(node.value, int) and \
                        not isinstance(node.value, float):
                    continue
                if node.lineno in checked_lines:
                    continue
                result.append((filename, node.lineno,
                               self.get_line(filename, node.lineno)))
                checked_lines.append(node.lineno)
        return result
