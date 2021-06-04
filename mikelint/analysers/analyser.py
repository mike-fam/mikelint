"""
Abstract analyser
"""
from functools import wraps
from inspect import getmembers, ismethod
from typing import Callable

from ..type_hints import AnalyserResults, AnalyserHelper
from ..utils import SyntaxTree, BaseViolation, ViolationResult


def register_check(error_format: str):
    """
    Registers a new checker to an analyser
    Args:
        error_format: error format of violation
    """
    def decorator(check_method: Callable):
        @wraps(check_method)
        def wrapper(*args, **kwargs):
            analyser = args[0]
            checker_name = check_method.__name__
            analyser.register_checker(checker_name,
                                      check_method.__doc__,
                                      error_format)
            result: list[ViolationResult] = check_method(*args, **kwargs)
            analyser.add_violations(checker_name, result)
        return wrapper
    return decorator


class Analyser:
    """Abstract base analyser"""
    def __init__(self, sources: dict[str, AnalyserHelper]):
        """
        Constructor
        Args:
            tree: syntax tree
            source: list of lines from source code
        """
        self._check_results: AnalyserResults = {}
        self._sources = sources

    def register_checker(self, name: str, description: str, error_format: str):
        """
        Registers a new checker to this analyser
        Args:
            name: name of the checker, typically the method name
            description: description of this checker
            error_format: format string used to display violations
        """
        self._check_results[name] = BaseViolation(description, error_format, [])

    def get_results(self) -> AnalyserResults:
        """
        Returns results of all checkers of this analyser
        """
        return self._check_results

    def add_violations(self, checker_name: str,
                       results: list[ViolationResult]) -> None:
        """
        Adds violation results to a checker
        Args:
            checker_name: name of the checker
            results: list of violation results
        """
        self._check_results[checker_name].values.extend(results)

    def get_line(self, file_name: str, line_number: int) -> str:
        """Returns line given line number"""
        return self._sources[file_name].source[line_number - 1].strip()

    def run(self):
        """
        Runs all checkers
        """
        for method_name, method in getmembers(self, predicate=ismethod):
            if not method_name.startswith("check_"):
                continue
            method()
