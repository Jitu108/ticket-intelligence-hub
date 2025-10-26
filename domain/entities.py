#domain/entities.py

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from .value_objects import Status, Priority, Email

@dataclass
class User:
    user_id: Optional[int]
    email: Email
    display_name: str
    role: str = "agent"
    created_utc: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Ticket:
    ticket_id: Optional[int]
    requester_id: int
    subject: str
    status: Status = Status.OPEN
    category: Optional[str] = None
    priority: Optional[Priority] = None
    llm_summary: Optional[str] = None
    created_utc: datetime = field(default_factory=datetime.utcnow)
    updated_utc: datetime = field(default_factory=datetime.utcnow)

@dataclass
class TicketMessage:
    message_id: Optional[int]
    ticket_id: int
    author_id: int
    body: str
    is_internal: bool = False
    created_utc: datetime = field(default_factory=datetime.utcnow)