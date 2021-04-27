from dataclasses import dataclass

from linter.type_hints import ViolationResult


@dataclass
class Violation:
    description: str
    format: str
    values: list[ViolationResult]
