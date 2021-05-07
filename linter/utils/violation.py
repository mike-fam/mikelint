"""
Anything violation related
"""
from dataclasses import dataclass
from typing import Union


ViolationResult = tuple[Union[str, int, float]]


@dataclass
class BaseViolation:
    """Represents a list of violations found after running the checkers"""
    description: str
    format: str
    values: list[ViolationResult]
