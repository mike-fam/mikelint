from pathlib import Path
from typing import Type

import yaml
from astroid import parse, Module

from .analysers import Analyser
from .formatters import Formatter
from .type_hints import AnalyserHelper
from .utils.tree import SyntaxTree
from .utils.violation import BaseViolation


class Run:
    def __init__(self, analysers: list[Type[Analyser]],
                 formatter: Type[Formatter],
                 source_file_names: list[str], config_file_name: str):
        self._analysers = analysers
        self._formatter_cls = formatter
        self._analyser_helpers: dict[str, AnalyserHelper] = {}
        for source_file_name in source_file_names:
            try:
                with open(source_file_name) as fin:
                    source = fin.read()
            except FileNotFoundError:
                print(f"{source_file_name} not found, skipping...")
                continue
            module: Module = parse(source)
            lines = source.splitlines()
            tree = SyntaxTree(module)
            filename = Path(source_file_name).name
            self._analyser_helpers[filename] = AnalyserHelper(tree, lines)

        with open(config_file_name) as config_file:
            self._config = yaml.load(config_file, Loader=yaml.SafeLoader)
        self._results: dict[str, dict[str, BaseViolation]] = {}
        # Uncomment to see source tree
        # print(module.repr_tree())

    def run(self):
        for analyser_cls in self._analysers:
            analyser = analyser_cls(self._analyser_helpers)
            analyser.run()
            self._results[analyser_cls.__name__] = analyser.get_results()

    def print_results(self):
        formatter = self._formatter_cls(self._config, self._results)
        print(formatter.format())

    def get_results(self):
        return self._results
