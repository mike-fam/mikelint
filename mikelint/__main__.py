import argparse

from .formatters import SimpleFormatter, JsonFormatter
from .analysers import (
    ClassInstanceAnalyser, DocstringAnalyser,
    EncapsulationAnalyser, NamingAnalyser,
    ScopeAnalyser, StructureAnalyser
)
from .run import Run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Configuration file",
                        required=True)
    parser.add_argument("-s", "--source", help="Source file",
                        required=True, action="append")
    parser.add_argument("-j", "--json", help="Display JSON output",
                        action="store_true", default=False)
    args = parser.parse_args()
    analysers = [
        ClassInstanceAnalyser,
        DocstringAnalyser,
        EncapsulationAnalyser,
        NamingAnalyser,
        ScopeAnalyser,
        StructureAnalyser
    ]
    runner = Run(analysers,
                 JsonFormatter if args.json else SimpleFormatter,
                 args.source,
                 args.config)
    runner.run()
    runner.print_results()


if __name__ == '__main__':
    main()
