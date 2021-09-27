import json

from ..utils import BaseViolation, DataclassJsonEncoder
from .formatter_ import Formatter


class JsonFormatter(Formatter):
    def format(self) -> str:
        output = {}
        for criteria_name, criteria in self._config.items():
            output[criteria_name] = criteria_result = {}
            for sub_criteria, analysers in criteria.items():
                criteria_result[sub_criteria] = self._format_criteria(analysers)

        return json.dumps(output, indent=4, cls=DataclassJsonEncoder)

    def _format_criteria(self, checkers: list[str]) -> list[dict]:
        """
        Returns a string containing useful information from the specified
        analyser

        Args:
            checkers: list of string representations of checkers, might be in
                the format of Analyser.checker or Analyser

        Returns: Meaningful string containing information of the checker(s).
        """
        output = []
        for analyser in checkers:
            analyser_name, _, checker_name = analyser.partition(".")
            if checker_name:
                output.append(self.serialise_violation(
                    self._check_output[analyser_name][checker_name]))
            else:
                for violation in self._check_output[analyser_name].values():
                    output.append(self.serialise_violation(violation))
        return output

    @staticmethod
    def serialise_violation(violation: BaseViolation):
        """
        Gets a meaningful string containing information about a violation

        Args:
            violation: BaseViolation information

        Returns: a meaningful string containing information about a violation
        """
        serialised_violation = {"description": violation.description,
                                "violations": []}
        for value in violation.values:
            serialised_violation["violations"].append(
                violation.format.format(*value))
        return serialised_violation
