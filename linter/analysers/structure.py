from linter.analysers.analyser import Analyser, register_check


class StructureAnalyser(Analyser):
    @register_check("Number of lines longer than {0} characters: {1}\n"
                    "\tLines {2} are longer than {0} characters")
    def check_line_length(self):
        long_lines_80 = [line_num + 1 for line_num, line in self._source
                         if len(line) > 80]
        long_lines_100 = [line_num + 1 for line_num, line in self._source
                          if len(line) > 100]
        long_lines_120 = [line_num + 1 for line_num, line in self._source
                          if len(line) > 120]
        return [(80, len(long_lines_80), ", ".join(long_lines_80)),
                (100, len(long_lines_80), ", ".join(long_lines_100)),
                (120, len(long_lines_80), ", ".join(long_lines_120)),
                ]
