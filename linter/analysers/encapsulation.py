from astroid import Attribute, Name, AssignAttr
from linter.analysers.analyser import Analyser, register_check


class EncapsulationAnalyser(Analyser):
    @register_check("Private attribute `{}` accessed outside class on line {}"
                    ":\n\t{}")
    def check_private_attribute_accessed_outside_class(self):
        """Checks if private attribute is accessed outside class """
        result: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, Attribute):
                continue
            if not node.attrname.startswith("_") or \
                    node.attrname.startswith("__"):
                continue
            expr = node.expr
            if isinstance(expr, Name) and expr.name == "self":
                continue
            result.append((node.attrname, node.lineno,
                           self.get_line(node.lineno)))
        return result

    @register_check("Private attribute `{}` defined outside class on line {}:\n"
                    "\t{}")
    def check_private_attribute_defined_outside_class(self):
        """Checks if private attribute is defined outside class """
        result: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignAttr):
                continue
            if not node.attrname.startswith("_") or \
                    node.attrname.startswith("__"):
                continue
            expr = node.expr
            if isinstance(expr, Name) and expr.name == "self":
                continue
            result.append((node.attrname, node.lineno,
                           self.get_line(node.lineno)))
        return result

    @register_check("Public attribute `{}` could have been private (line {}):"
                    "\n\t{}")
    def check_public_attribute_defined_self(self):
        """Checks if public attribute could be replaced by a private attribute """
        result: list[tuple[str, int, str]] = []
        for node in self._tree.pre_order():
            if not isinstance(node, AssignAttr):
                continue
            if node.attrname.startswith("_") and \
                    not node.attrname.startswith("__"):
                continue
            expr = node.expr
            if not (isinstance(expr, Name) and expr.name == "self"):
                continue
            result.append((node.attrname, node.lineno,
                           self.get_line(node.lineno)))
        return result

