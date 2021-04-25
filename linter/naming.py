from linter.analyser import Analyser
import re


class NamingAnalyser(Analyser):
    SNAKE_CASE = re.compile(r"[a-z_][a-z0-9_]{2,30}$")
    CONSTANT_SNAKE_CASE = re.compile(r"(([A-Z_][A-Z0-9_]*)|(__.*__))$")

    def check_variable_name(self):
        pass