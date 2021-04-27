from linter.type_hints import Config, CheckOutput
from linter.violation import Violation


class Formatter:
    def __init__(self, config: Config, check_output: CheckOutput):
        """
        Constructor
        Args:
            config:
            check_output:
        """
        self._config = config
        self._check_output = check_output

    def format(self) -> str:
        raise NotImplementedError

    @staticmethod
    def _indent(multiline_str: str, indent=4):
        return ("\n" + " " * indent).join(multiline_str.splitlines())

    @staticmethod
    def _new_line(string: str):
        return string + "\n"

    @staticmethod
    def format_violation(violation: Violation):
        output = Formatter._new_line(violation.description)
        for format_values in violation.values:
            output += Formatter._new_line(
                Formatter._indent(violation.format.format(*format_values)))
        if not violation.values:
            output += Formatter._new_line(Formatter._indent("No violations "
                                                            "found"))
        return output

