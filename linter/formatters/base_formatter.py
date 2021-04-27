from linter.formatters.formatter import Formatter

BLOCK_WIDTH = 80
HORIZONTAL_BORDER = "-" * (BLOCK_WIDTH - 2)
BLOCK_TEMPLATE = """\
/{0}\\
|{{:^{1}}}|
\\{0}/\
""".format(HORIZONTAL_BORDER, BLOCK_WIDTH - 2)


class BaseFormatter(Formatter):
    def format(self) -> str:
        output = ""
        for criteria_name, criteria in self._config.items():
            output += self._new_line(BLOCK_TEMPLATE.format(criteria_name))
            for index, (sub_criteria, analysers) in \
                    enumerate(criteria.items(), start=1):
                output += self._new_line(self._indent(
                    self._format_criteria(index, sub_criteria, analysers)))
                if index < len(criteria):
                    output += self._new_line(HORIZONTAL_BORDER)
        output += HORIZONTAL_BORDER
        return output

    def _format_criteria(self, index: int, sub_criteria: str,
                         analysers: list[str]):
        output = self._new_line(f"{index}. {sub_criteria}")
        for analyser in analysers:
            analyser_name, _, checker_name = analyser.partition(".")
            if checker_name:
                output += self._new_line(self._indent(self.format_violation(
                    self._check_output[analyser_name][checker_name])))
            else:
                for violation in \
                        self._check_output[analyser_name].values():
                    output += self._new_line(self._indent(
                        self.format_violation(violation)))
        if not analysers:
            output += self._new_line("None")
        return output
