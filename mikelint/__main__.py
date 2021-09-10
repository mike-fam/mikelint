import argparse

from .formatters import BaseFormatter
from .analysers import ClassInstanceAnalyser, DocstringAnalyser, EncapsulationAnalyser, NamingAnalyser, \
    ScopeAnalyser, StructureAnalyser
from .run import Run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Configuration file",
                        required=True)
    parser.add_argument("-s", "--source", help="Source file",
                        required=True, action="append")
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
