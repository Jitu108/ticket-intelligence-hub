# application/dtos.py
from pydantic import BaseModel, Field
from typing import Optional, List

class CreateTicketDTO(BaseModel):
    requester_email: str
    subject: str
    body: str

class TicketViewDTO(BaseModel):
    ticket_id: int
    subject: str
    status: str
    category: Optional[str]
    priority: Optional[str]
    llm_summary: Optional[str]
    messages: List[str] = Field(default_factory=list)

