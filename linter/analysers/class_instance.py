"""
Analyser for class vs instance usage
"""
from astroid import ClassDef, Call, Attribute, Name
from .analyser import Analyser, register_check


class ClassInstanceAnalyser(Analyser):
    """Checks violations in class vs instance usages"""
    @register_check("{}:{}: Method call treated as function instead of "
                    "member of instance:\n\t{}")
    def check_method_call(self):
        """Checks if method call is treated as regular function instead of
        member of class instance"""
        # filename, lineno, line
        result: list[tuple[str, int, str]] = []
        class_names: list[str] = []
        for filename, attr in self._sources.items():
            tree = attr.tree
            for node in tree.pre_order():
                if not isinstance(node, ClassDef):
                    continue
                class_names.append(node.name)

            for node in tree.pre_order():
                if not isinstance(node, Call):
                    continue
                func = node.func
                if not isinstance(func, Attribute):
                    continue
                if not isinstance(func.expr, Name):
                    continue
                if func.expr.name in class_names:
                    result.append((filename, node.lineno, node.as_string()))
        return result
