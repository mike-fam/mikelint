from astroid import parse, Module
import pprint

from linter.analysers.class_instance import ClassInstanceAnalyser
from linter.analysers.docstrings import DocstringAnalyser
from linter.analysers.encapsulation import EncapsulationAnalyser
from linter.analysers.naming import NamingAnalyser
from linter.analysers.scope import ScopeAnalyser
from linter.analysers.structure import StructureAnalyser
from linter.tree import SyntaxTree


def main():
    with open("resources/test2.py") as fin:
        source = fin.read()
    module: Module = parse(source)
    lines = source.splitlines()
    # pprint.pprint(lines)
    # print("-" * 200)
    # members = module.body
    # for member in members:
    #     if isinstance(member, ast.ClassDef):
    #         print(member.body)
    print(module.repr_tree())
    # print("-" * 200)
    tree = SyntaxTree(module)
    analyser = ClassInstanceAnalyser(tree, lines)
    analyser.run()
    pprint.pprint(analyser.get_results(), width=200)

    # analyser.check_variable_snake_case()


if __name__ == '__main__':
    main()
