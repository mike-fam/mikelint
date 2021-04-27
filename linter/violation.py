from dataclasses import dataclass
from typing import Union


ViolationResult = tuple[Union[str, int, float]]


@dataclass
class Violation:
    description: str
    format: str
    values: list[ViolationResult]
