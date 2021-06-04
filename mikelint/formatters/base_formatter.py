"""
A simple formatter to display analyser output in similar format as testrunner
"""
from .formatter_ import Formatter
from ..utils import new_line, indent, BaseViolation

BLOCK_WIDTH = 80
HORIZONTAL_BORDER = "-" * (BLOCK_WIDTH - 2)
BLOCK_TEMPLATE = """\
/{0}\\
|{{:^{1}}}|
\\{0}/\
""".format(HORIZONTAL_BORDER, BLOCK_WIDTH - 2)


class BaseFormatter(Formatter):
    """Simple formatter with output similar to testrunner"""
    def format(self) -> str:
        output = ""
        for criteria_name, criteria in self._config.items():
            output += new_line(BLOCK_TEMPLATE.format(criteria_name))
            for index, (sub_criteria, analysers) in \
                    enumerate(criteria.items(), start=1):
                output += new_line(indent(
                    self._format_criteria(index, sub_criteria, analysers)))
                if index < len(criteria):
                    output += new_line(HORIZONTAL_BORDER)
        output += HORIZONTAL_BORDER
        return output

    def _format_criteria(self, index: int, sub_criteria: str,
                         checkers: list[str]):
        """
        Returns a string containing useful information from the specified
        analyser

        Args:
            index: index of the sub criteria
            sub_criteria: name of sub criteria
            checkers: list of string representations of checkers, might be in
                the format of Analyser.checker or Analyser

        Returns: Meaningful string containing information of the checker(s).
        """
        output = new_line(f"{index}. {sub_criteria}")
        for analyser in checkers:
            analyser_name, _, checker_name = analyser.partition(".")
            if checker_name:
                output += new_line(indent(self.format_violation(
                    self._check_output[analyser_name][checker_name])))
            else:
                for violation in self._check_output[analyser_name].values():
                    output += new_line(indent(self.format_violation(violation)))
        if not checkers:
            output += new_line("None")
        return output

    @staticmethod
    def format_violation(violation: BaseViolation):
        """
        Gets a meaningful string containing information about a violation

        Args:
            violation: BaseViolation information

        Returns: a meaningful string containing information about a violation
        """
        output = new_line(violation.description)
        for format_values in violation.values:
            output += new_line(indent(violation.format.format(*format_values)))
        if not violation.values:
            output += new_line(indent("No violations found"))
        return output
