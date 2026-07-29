from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    id: int
    name: str
    completed: bool = False
    description: str | None = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("name cannot be empty")
        if self.id < 0:
            raise ValueError("id cannot be less than 0")
