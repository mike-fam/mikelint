"""Docstring analyser"""
from typing import Optional
from astroid import ClassDef, FunctionDef
from docstring_parser import parse, Style

from .analyser import Analyser, register_check


class DocstringAnalyser(Analyser):
    """Analyses anything docstring related"""
    @register_check("{}:{}: Class {} missing docstring")
    def check_class_docstrings(self):
        """Checks if classes missing docstrings """
        result: list[tuple[str, int, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, ClassDef):
                    continue
                if node.doc:
                    continue
                result.append((filename, node.lineno, node.name,))
        return result

    @register_check("{}:{}: Method/Function {} missing docstring")
    def check_methods_function_docstrings(self):
        """Checks if methods or functions missing docstrings """
        result: list[tuple[str, int, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, FunctionDef):
                    continue
                if node.doc:
                    continue
                result.append((filename, node.lineno,
                               self._get_method_name(node)))
        return result

    @register_check("{}:{}: Missing/extra fields in docstrings of "
                    "function/method:\n"
                    "\tFunction/Method name: {}\n"
                    "\tMissing fields: {}\n"
                    "\tExtra fields: {}\n")
    def check_method_docstring_unexpected_missing(self):
        """Checks if docstring has missing or extra fields """
        result: list[tuple[str, int, str, str, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, FunctionDef):
                    continue
                signatures = self._get_expected_and_actual_method_parameters(node)
                if signatures is None:
                    continue
                method_name = self._get_method_name(node)
                expected, actual = signatures
                unexpected = [arg for arg, _ in actual]
                missing = []
                for arg, _ in expected:
                    try:
                        unexpected.remove(arg)
                    except ValueError:
                        missing.append(arg)
                if not unexpected and not missing:
                    continue
                result.append((filename, node.lineno, method_name,
                               ", ".join(missing) or "None",
                               ", ".join(unexpected) or "None"))
        return result

    @staticmethod
    def _get_expected_and_actual_method_parameters(node: FunctionDef) -> \
            (list[tuple[str, Optional[str]]], list[tuple[str, Optional[str]]]):
        if not node.doc:
            return None
        try:
            docstring = parse(node.doc, Style.google)
        except:
            return None
        actual = [(param.arg_name, param.type_name)
                  for param in docstring.params]
        expected = [(arg.name, annotation.as_string())
                    for arg, annotation in zip(node.args.args,
                                               node.args.annotations)
                    if annotation is not None]
        # Remove 'self' from expected signature
        if isinstance(node.parent, ClassDef):
            try:
                expected.pop(0)
            except IndexError:
                # for problems such as
                # class A:
                #     def method():  # no self here
                # idek why they do this, but they did
                pass

        return expected, actual

    @staticmethod
    def _get_method_name(node: FunctionDef):
        method_name = node.name
        parent = node.parent
        if isinstance(parent, ClassDef):
            method_name = f"{parent.name}.{method_name}"
        return method_name

    @register_check("{}:{}: Missing parameter types in docstrings of "
                    "function/method:"
                    "\n\tFunction/Method name: {}\n"
                    "\tFields that lack param type: {}\n")
    def check_method_docstring_missing_type(self):
        """Checks if docstrings have all the parameter types necessary"""
        # method_name, lineno, fields
        results: list[tuple[str, int, str, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, FunctionDef):
                    continue
                signatures = self._get_expected_and_actual_method_parameters(node)
                if signatures is None:
                    continue
                method_name = self._get_method_name(node)
                expected, actual = signatures
                expected = dict(expected)
                actual = dict(actual)
                fields = []
                for name, type_ in actual.items():
                    if name not in expected:
                        continue
                    if type_ is None and expected[name] is None:
                        fields.append(name)
                if fields:
                    results.append((filename, node.lineno, method_name,
                                    ", ".join(fields)))
        return results

    @register_check("{}:{}: Cannot parse docstring of function/method:\n"
                    "\t{}")
    def check_docstring_correct_format(self):
        """Checks if docstring can be parsed correctly """
        result: list[tuple[str, int, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, FunctionDef):
                    continue
                if not node.doc:
                    continue
                method_name = self._get_method_name(node)
                try:
                    parse(node.doc, Style.google)
                except:
                    result.append((filename, node.lineno, method_name))
        return result
