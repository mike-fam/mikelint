from astroid import parse, Module

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
    for node in tree.post_order():
        print(node)


if __name__ == '__main__':
    main()
