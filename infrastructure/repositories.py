#infrastructure/repositories.py

from typing import List, Optional
from .mappers import row_to_user, row_to_ticket, row_to_message
from ..domain.entities import User, Ticket, TicketMessage
from ..domain.value_objects import Email

class UserRepository:
    def __init__(self, conn): self.conn = conn

    def get_by_email(self, email: Email) -> Optional[User]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT user_id, email, display_name, role, created_utc FROM dbo.AppUser WHERE email=?", (str(email),))
        row = cursor.fetchone()
        return row_to_user(row) if row else None
    
    def add(self, user: User) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO dbo.AppUser (email, display_name, role) VALUES (?, ?, ?)",
            user.email.value, user.display_name, user.role
        )
        cursor.execute("SELECT TOP 1 user_id FROM dbo.AppUser WHERE email=? ORDER BY created_utc DESC", (user.email.value,))
        user_id = cursor.fetchone()[0]
        return user_id
    
class TicketRepository:
    def __init__(self, conn): self.conn = conn

    def get(self, ticket_id: int) -> Optional[Ticket]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT ticket_id, requester_id, subject, status, category, priority, llm_summary, created_utc, updated_utc FROM dbo.Ticket WHERE ticket_id=?", (ticket_id,))
        row = cursor.fetchone()
        return row_to_ticket(row) if row else None
    
    def add(self, ticket: Ticket) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO dbo.Ticket (requester_id, subject, status, category, priority, llm_summary)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            ticket.requester_id, ticket.subject, ticket.status.value,
            ticket.category,
            ticket.priority.value if ticket.priority else None,
            ticket.llm_summary
        )
        cursor.execute("SELECT TOP 1 ticket_id FROM dbo.Ticket ORDER BY created_utc DESC")
        ticket_id = cursor.fetchone()[0]
        print("Created ticket with ID:", ticket_id)
        return ticket_id
    
    def update_summary(self, ticket_id: int, summary: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE dbo.Ticket SET llm_summary=? WHERE ticket_id=?",
            (summary, ticket_id)
        )

class MessageRepository:
    def __init__(self, conn): self.conn = conn

    def list_by_ticket(self, ticket_id: int) -> List[TicketMessage]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT message_id, ticket_id, author_id, body, is_internal, created_utc FROM dbo.TicketMessage WHERE ticket_id=?", (ticket_id,))
        rows = cursor.fetchall()
        return [row_to_message(row) for row in rows]
    
    def add(self, message: TicketMessage) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO dbo.TicketMessage (ticket_id, author_id, body, is_internal)
            VALUES (?, ?, ?, ?)
            """,
            (message.ticket_id, message.author_id, message.body, message.is_internal)
        )
        cursor.execute("SELECT CAST(SCOPE_IDENTITY() AS BIGINT)")
        message_id = cursor.fetchone()[0]
        return message_id

