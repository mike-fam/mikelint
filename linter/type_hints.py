"""
Type hints helpers
"""
from linter.utils.violation import BaseViolation


CriteriaConfig = dict[str, list]

Config = dict[str, CriteriaConfig]

CheckOutput = dict[str, dict[str, BaseViolation]]
