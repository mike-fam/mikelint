"""Naming analyser, checks everything name related"""
import re
from astroid import AssignName, AssignAttr, For, Call, FunctionDef

from linter.analysers.analyser import Analyser, register_check


class NamingAnalyser(Analyser):
    """Analyse good naming"""
    SNAKE_CASE = re.compile(r"[a-z_][a-z0-9_]{0,30}$")
    CONSTANT_SNAKE_CASE = re.compile(r"(([A-Z_][A-Z0-9_]*)|(__.*__))$")
    # FIXME: might give false positives
    HUNGARIAN_NOTATION = re.compile(r"(str|string|int|list|lst|dict|dictionary|"
                                    r"tup|tuple|float|func|function|method)")

    @register_check(error_format="Non snake-case variable '{}' defined on line "
                                 "{}:\n\t{}")
    def check_variable_snake_case(self):
        """Checks for non snake-case variable naming """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignName):
                continue

            # Ignore constants
            if node.parent is self._tree.get_root():
                continue

            if self.SNAKE_CASE.fullmatch(node.name):
                continue
            results.append((node.name, node.lineno,
                            node.parent.as_string().splitlines()[0]))
        return results

    @register_check(error_format="Non snake-case function/method name '{}' "
                                 "defined on line {}:\n\t{}")
    def check_method_snake_case(self):
        """Checks for non snake-case function and method naming """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, FunctionDef):
                continue
            if self.SNAKE_CASE.fullmatch(node.name):
                continue
            results.append((node.name, node.lineno,
                            node.as_string().strip().splitlines()[0]))
        return results

    @register_check(error_format="Non snake-case attribute '{}' defined on "
                                 "line {}:\n\t{}")
    def check_attribute_snake_case(self):
        """Checks for non snake-case attrbute naming """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignAttr):
                continue
            if self.SNAKE_CASE.fullmatch(node.attrname):
                continue
            results.append((node.attrname, node.lineno,
                            node.parent.as_string().splitlines()[0]))
        return results

    @register_check(error_format="Potential bad variable name '{}' defined on "
                                 "line {}:\n\t{}")
    def check_potential_bad_variable_names(self):
        """Checks for potential bad naming, i.e. names with 1-2 characters """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignName):
                continue

            # skip naming for `for i in range`
            if self._is_for_range_variable(node) \
                    and node.name in ["i", "j", "k"]:
                continue

            if len(node.name) >= 3:
                continue

            results.append((node.name, node.lineno,
                            node.parent.as_string().splitlines()[0]))
        return results

    @register_check(error_format="Hungarian notation variable '{}' used on "
                                 "line {}:\n\t{}")
    def check_hungarian_notation_variable(self):
        """Checks for variable names with hungarian notation """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignName):
                continue
            if not self.HUNGARIAN_NOTATION.search(node.name):
                continue
            results.append((node.name, node.lineno,
                            node.parent.as_string().splitlines()[0]))
        return results

    @register_check(error_format="Hungarian notation attribute '{}' used on "
                                 "line {}:\n\t{}")
    def check_hungarian_notation_attribute(self):
        """Checks for attribute names with hungarian notation """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignAttr):
                continue
            if not self.HUNGARIAN_NOTATION.search(node.attrname):
                continue
            results.append((node.attrname, node.lineno,
                            node.parent.as_string().splitlines()[0]))
        return results

    @register_check(error_format="Hungarian notation in function/method name"
                                 " '{}' defined on line {}:\n\t{}")
    def check_hungarian_notation_method(self):
        """Checks for hungarian notation function and method naming """
        results: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, FunctionDef):
                continue
            if not self.HUNGARIAN_NOTATION.search(node.name):
                continue
            results.append((node.name, node.lineno,
                            node.as_string().strip().splitlines()[0]))
        return results

    @register_check("Line {}: Variables defined at global scope should be "
                    "treated as constants:\n\t{}")
    def check_constant_naming(self):
        """Checks if constants are named in UPPER_SNAKE_CASE"""
        # lineno, line
        results: list[tuple[int, str]] = []
        for node in self._tree.get_root().get_children():
            if not isinstance(node, AssignName):
                continue
            if not self.CONSTANT_SNAKE_CASE.fullmatch(node.name):
                continue
            results.append((node.lineno, node.as_string()))
        return results

    @staticmethod
    def _is_for_range_variable(node: AssignName):
        """Check if the assignment is for a variable for a for range loop """
        parent = node.parent
        if not isinstance(parent, For):
            return False
        iter_on = parent.iter
        if not isinstance(iter_on, Call):
            return False
        return iter_on.func.as_string() == "range"
