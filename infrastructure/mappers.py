# infrastructure/mappers.py

from ..domain.entities import User, Ticket, TicketMessage
from ..domain.value_objects import Status, Priority, Email

def row_to_user(row) -> User:
    return User(
        user_id=row[0], 
        email=Email(row[1]), 
        display_name=row[2], 
        role=row[3])

def row_to_ticket(row) -> Ticket:
    priority = Priority(row[5]) if row[5] is not None else None
    return Ticket(
        ticket_id=row[0],
        requester_id=row[1],
        subject=row[2],
        status=Status(row[3]),
        category=row[4],
        priority=priority,
        llm_summary=row[6],
        created_utc=row[7],
        updated_utc=row[8]
    )

def row_to_message(row) -> TicketMessage:
    return TicketMessage(
        message_id=row[0],
        ticket_id=row[1],
        author_id=row[2],
        body=row[3],
        is_internal=row[4],
        created_utc=row[5]
    )