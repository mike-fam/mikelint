from functools import wraps
from inspect import getmembers, ismethod
from typing import Callable

from linter.analysers.analyse_error import CheckError
from linter.tree import SyntaxTree
from linter.type_hints import Violation, ViolationResult


def register_check(error_format: str):
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
    def __init__(self, tree: SyntaxTree):
        """

        Args:
            tree:
        """
        self._tree = tree
        self._check_results: dict[str, Violation] = {}
        # TODO: manage tree
        #   manage rules, maybe config file

    @staticmethod
    def check(condition: bool, message: str):
        if not condition:
            raise CheckError(message)

    def register_checker(self, name, description, error_format):
        self._check_results[name] = {
            "format": error_format,
            "description": description,
            "values": []
        }

    def get_results(self) -> dict[str, Violation]:
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
        self._check_results[checker_name]["values"].extend(results)

    def run(self):
        """
        Runs all checkers
        """
        for method_name, method in getmembers(self, predicate=ismethod):
            if not method_name.startswith("check_"):
                continue
            method()
