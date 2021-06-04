"""
Analyse encapsulation violations
"""
from astroid import Attribute, Name, AssignAttr

from .analyser import Analyser, register_check


class EncapsulationAnalyser(Analyser):
    """
    Encapsulation analyser, checks if class members follow best
    access control practices
    """
    @register_check("{}:{}: Private attribute `{}` accessed outside class:\n"
                    "\t{}")
    def check_private_attribute_accessed_outside_class(self):
        """Checks if private attribute is accessed outside class """
        result: list[tuple[str, int, str, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, Attribute):
                    continue
                if not node.attrname.startswith("_") or \
                        node.attrname.startswith("__"):
                    continue
                expr = node.expr
                if isinstance(expr, Name) and expr.name == "self":
                    continue
                result.append((filename, node.lineno, node.attrname,
                               self.get_line(filename, node.lineno)))
        return result

    @register_check("{}:{}: Private attribute `{}` defined outside class:\n"
                    "\t{}")
    def check_private_attribute_defined_outside_class(self):
        """Checks if private attribute is defined outside class """
        result: list[tuple[str, int, str, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, AssignAttr):
                    continue
                if not node.attrname.startswith("_") or \
                        node.attrname.startswith("__"):
                    continue
                expr = node.expr
                if isinstance(expr, Name) and expr.name == "self":
                    continue
                result.append((filename, node.lineno, node.attrname,
                               self.get_line(filename, node.lineno)))
        return result

    @register_check("{}:{}: Public attribute `{}` could have been private:\n"
                    "\t{}")
    def check_public_attribute_defined_self(self):
        """Checks if public attribute could be replaced by a private attribute """
        result: list[tuple[str, int, str, str]] = []
        for filename, attr in self._sources.items():
            for node in attr.tree.pre_order():
                if not isinstance(node, AssignAttr):
                    continue
                if node.attrname.startswith("_") and \
                        not node.attrname.startswith("__"):
                    continue
                expr = node.expr
                if not (isinstance(expr, Name) and expr.name == "self"):
                    continue
                result.append((filename, node.lineno, node.attrname,
                               self.get_line(filename, node.lineno)))
        return result
