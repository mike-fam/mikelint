from linter.analysers.analyser import Analyser, register_check

from astroid.mixins import BlockRangeMixIn
from astroid.node_classes import NodeNG
from astroid import Pass


class StructureAnalyser(Analyser):
    @register_check("Number of lines longer than {0} characters: {1}\n"
                    "\tLines {2} are longer than {0} characters")
    def check_line_length(self):
        """ Checks if code has any line that's too long """
        # character_count, number_of_lines, line_numbers
        result: list[tuple[int, int, str]] = []
        for length in [80, 100, 120, 140]:
            long_lines = [str(line_num + 1)
                          for line_num, line in enumerate(self._source)
                          if len(line) > length]
            result.append((length, len(long_lines),
                           ", ".join(long_lines) or None))
        return result

    @register_check("Lines ({}-{}): too many nested control structures\n{}")
    def check_structure_complexity(self):
        """Checks if control structures are nested too deeply"""
        # line_start, line_end, block
        result: list[tuple[int, int, str]] = []
        complexities: dict[NodeNG, int] = {}
        for node in self._tree.post_order():
            if not isinstance(node, BlockRangeMixIn):
                continue
            complexities[node] = 1 + max((complexities.get(child, 0)
                                          for child in node.get_children()),
                                         default=0)

        for node, complexity in complexities.items():
            if complexity < 4:
                continue
            highest_node = node
            while complexities.get(highest_node.parent) is not None:
                highest_node = highest_node.parent
            start, end = highest_node.block_range(highest_node.lineno)
            result.append((start, end, "\n".join(self._source[start - 1:end])))
        return result

    @register_check("Line {}: Control structure block does nothing\n")
    def check_structure_empty(self):
        """Checks if control structures blocks just have `pass` in them"""
        # line_start, line_end, block
        result: list[tuple[int]] = []
        for node in self._tree.post_order():
            if not isinstance(node, BlockRangeMixIn):
                continue
            if len(node.body) == 1 and isinstance((pass_ := node.body[0]),
                                                  Pass):
                result.append((pass_.lineno))
            elif getattr(node, "orelse", None) is not None and \
                    len(node.orelse) == 1 and \
                    isinstance((pass_ := node.orelse[0]), Pass):
                result.append((pass_.lineno))
        return result

