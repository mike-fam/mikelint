"""
Type hints helpers
"""
from linter.utils.violation import BaseViolation


CriteriaConfig = dict[str, list]

Config = dict[str, CriteriaConfig]

AnalyserResults = dict[str, BaseViolation]

CheckOutput = dict[str, AnalyserResults]
