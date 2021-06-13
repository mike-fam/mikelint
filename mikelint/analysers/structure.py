"""
Analyses code structure
"""
from astroid.mixins import BlockRangeMixIn
from astroid.node_classes import NodeNG
from astroid import Pass, TryExcept

from .analyser import Analyser, register_check


class StructureAnalyser(Analyser):
    """Structure analyser, checks if general structure is ok"""

    @register_check("{3}: Number of lines longer than {0} characters: {1}\n"
                    "\tLines {2} are longer than {0} characters")
    def check_line_length(self):
        """Checks if code has any line that's too long """
        # character_count, number_of_lines, line_numbers
        result: list[tuple[int, int, str, str]] = []
        for filename, attr in self._sources.items():
            for length in [80, 100, 120, 140]:
                long_lines = [str(line_num + 1)
                              for line_num, line in enumerate(attr.source)
                              if len(line.rstrip()) > length]
                if not long_lines:
                    continue
                result.append((length, len(long_lines),
                               ", ".join(long_lines) or None,
                               filename))
        return result

    @register_check("{}:{}-{}: too many nested control structures\n{}")
    def check_structure_complexity(self):
        """Checks if control structures are nested too deeply"""
        # line_start, line_end, block
        result: list[tuple[str, int, int, str]] = []
        for filename, attr in self._sources.items():
            complexities: dict[NodeNG, int] = {}
            for node in attr.tree.post_order():
                if not isinstance(node, BlockRangeMixIn):
                    continue
                children = node.body.copy()
                if isinstance(node, TryExcept):
                    children.extend(node.handlers)
                if hasattr(node, "orelse") and len(node.orelse) > 1:
                    children.extend(child for child in node.orelse)
                complexities[node] = 1 + max((complexities.get(child, 0)
                                              for child in node.body),
                                             default=0)
            checked_nodes = []
            for node, complexity in complexities.items():
                if complexity < 4:
                    continue
                highest_node = node
                while complexities.get(highest_node.parent) is not None:
                    highest_node = highest_node.parent
                if highest_node in checked_nodes:
                    continue
                start, end = highest_node.block_range(highest_node.lineno)
                result.append((filename, start, end,
                               "\n".join(attr.source[start - 1:end])))
                checked_nodes.append(highest_node)
        return result

    @register_check("{}:{}: Control structure block does nothing\n")
    def check_structure_empty(self):
        """Checks if control structures blocks just have `pass` in them"""
        # line_start, line_end, block
        result: list[tuple[str, int]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.post_order():
                if not isinstance(node, BlockRangeMixIn):
                    continue
                if len(node.body) == 1 and \
                        isinstance((pass_ := node.body[0]), Pass):
                    result.append((filename, pass_.lineno))
                elif getattr(node, "orelse", None) is not None and \
                        len(node.orelse) == 1 and \
                        isinstance((pass_ := node.orelse[0]), Pass):
                    result.append((filename, pass_.lineno))
        return result
