from typing import Type

from astroid import parse, Module
import argparse
import yaml

from linter.analysers.analyser import Analyser
from linter.analysers.class_instance import ClassInstanceAnalyser
from linter.analysers.docstrings import DocstringAnalyser
from linter.analysers.encapsulation import EncapsulationAnalyser
from linter.analysers.naming import NamingAnalyser
from linter.analysers.scope import ScopeAnalyser
from linter.analysers.structure import StructureAnalyser
from linter.formatters.base_formatter import BaseFormatter
from linter.formatters.formatter import Formatter
from linter.tree import SyntaxTree
from linter.violation import Violation


class Run:
    def __init__(self, analysers: list[Type[Analyser]],
                 formatter: Type[Formatter],
                 source_file_name: str, config_file_name: str):
        self._analysers = analysers
        self._formatter_cls = formatter
        with open(source_file_name) as fin:
            source = fin.read()
        module: Module = parse(source)
        self._lines = source.splitlines()
        self._tree = SyntaxTree(module)
        with open(config_file_name) as config_file:
            self._config = yaml.load(config_file, Loader=yaml.SafeLoader)
        self._results: dict[str, dict[str, Violation]] = {}

    def run(self):
        for analyser_cls in self._analysers:
            analyser = analyser_cls(self._tree, self._lines)
            analyser.run()
            self._results[analyser_cls.__name__] = analyser.get_results()

    def print_results(self):
        formatter = self._formatter_cls(self._config, self._results)
        print(formatter.format())

    def get_results(self):
        return self._results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Configuration file",
                        required=True)
    parser.add_argument("-s", "--source", help="Source file",
                        required=True)
    args = parser.parse_args()
    analysers = [
        ClassInstanceAnalyser,
        DocstringAnalyser,
        EncapsulationAnalyser,
        NamingAnalyser,
        ScopeAnalyser,
        StructureAnalyser
    ]
    runner = Run(analysers, BaseFormatter, args.source, args.config)
    runner.run()
    runner.print_results()


if __name__ == '__main__':
    main()
