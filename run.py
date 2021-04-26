from astroid import parse, Module
import pprint
from linter.analysers.naming import NamingAnalyser
from linter.tree import SyntaxTree


def main():
    with open("resources/test.py") as fin:
        module: Module = parse(fin.read())
    # members = module.body
    # for member in members:
    #     if isinstance(member, ast.ClassDef):
    #         print(member.body)
    print(module.repr_tree())
    tree = SyntaxTree(module)
    analyser = NamingAnalyser(tree)
    analyser.run()
    pprint.pprint(analyser.get_results())

    # analyser.check_variable_snake_case()


if __name__ == '__main__':
    main()
