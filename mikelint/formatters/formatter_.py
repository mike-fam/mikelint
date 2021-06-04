"""
Abstract formatter
Used to convert error outputs to user friendly output to be displayed on user
interface
"""
from ..type_hints import Config, CheckOutput


class Formatter:
    """Abstract formatter"""
    def __init__(self, config: Config, check_output: CheckOutput):
        """
        Constructor
        Args:
            config: configuration file that links criteria to tests
            check_output: output from checkers
        """
        self._config = config
        self._check_output = check_output

    def format(self) -> str:
        """Returns formatted string to be displayed on screen"""
        raise NotImplementedError

    def get_config(self) -> Config:
        """Returns configuration object"""
        return self._config

    def get_check_output(self):
        """Returns check output from analysers"""
        return self._check_output
