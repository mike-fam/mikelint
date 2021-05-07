"""
Analyser for class vs instance usage
"""
from astroid import ClassDef, Call, Attribute, Name
from linter.analysers.analyser import Analyser, register_check


class ClassInstanceAnalyser(Analyser):
    """Checks violations in class vs instance usages"""
    @register_check("Line {}: Method call treated as function instead of "
                    "member of instance:\n\t{}")
    def check_method_call(self):
        """Checks if method call is treated as regular function instead of
                member of class instance"""
        # lineno, line
        result: list[tuple[int, str]] = []
        class_names: list[str] = []
        for node in self._tree.pre_order():
            if not isinstance(node, ClassDef):
                continue
            class_names.append(node.name)

        for node in self._tree.pre_order():
            if not isinstance(node, Call):
                continue
            func = node.func
            if not isinstance(func, Attribute):
                continue
            if not isinstance(func.expr, Name):
                continue
            if func.expr.name in class_names:
                result.append((node.lineno, node.as_string()))
        return result
