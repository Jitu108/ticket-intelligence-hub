# domain/value_objects.py

from enum import Enum
from dataclasses import dataclass

class Status(str, Enum):
    OPEN = "open"
    PENDING = "pending"
    CLOSED = "closed"


class Priority(str, Enum):  
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    # URGENT = "urgent"

@dataclass(frozen=True)
class Email:
    value: str
    def __post_init__(self):
        # if "@" not in self.value or "." not in self.value.split("@")[-1]:
        #     raise ValueError(f"Invalid email address: {self.value}")
        if "@" not in self.value:
            raise ValueError("Invalid email")