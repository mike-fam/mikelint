from linter.violation import Violation

CriteriaConfig = dict[str, list]

Config = dict[str, CriteriaConfig]

CheckOutput = dict[str, dict[str, Violation]]
