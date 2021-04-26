from typing import TypedDict, Union


ViolationResult = tuple[Union[str, int, float]]


class Violation(TypedDict):
    format: str
    values: list[ViolationResult]
    description: str
