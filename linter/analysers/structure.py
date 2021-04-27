import pprint

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
            result.append((length, len(long_lines), ", ".join(long_lines)))
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

    @register_check("Line {}: Control block does nothing\n\t{}")
    def check_structure_empty(self):
        """Checks if control structures blocks just have `pass` in them"""
        # line_start, line_end, block
        result: list[tuple[int, str]] = []
        complexities: dict[NodeNG, int] = {}
        for node in self._tree.post_order():
            if not isinstance(node, BlockRangeMixIn):
                continue
            children = list(node.body)
            if len(children) == 1 and isinstance(children[0], Pass):
                result.append((node.lineno, node.as_string()))
        return result

