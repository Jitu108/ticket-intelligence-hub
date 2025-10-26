# application/services.py
from typing import Tuple
from ..domain.entities import Ticket, TicketMessage, User
from ..domain.value_objects import Email, Status
from .dtos import CreateTicketDTO, TicketViewDTO
from ..infrastructure.repositories import UserRepository, TicketRepository, MessageRepository
from ..infrastructure.llm import BaseLLM
from ..infrastructure.embedding import EmbeddingStrategy

class TicketService:
    def __init__(self, llm: BaseLLM, embedder: EmbeddingStrategy):
        self.llm = llm
        self.embedder = embedder

    def create_ticket(self, conn, dto: CreateTicketDTO) -> int:
        print("Creating ticket for:", dto.requester_email)
        users = UserRepository(conn)
        tickets = TicketRepository(conn)
        messages = MessageRepository(conn)

        # 1) Resolve or create user
        user = users.get_by_email(dto.requester_email)
        print("Resolved user:", user)
        if not user:
            print("User not found, creating new user.")
            user = User(user_id=None, 
                        email=Email(dto.requester_email),
                        display_name=dto.requester_email.split("@")[0].title(), 
                        role="end_user")
            print("Creating new user:", user)
            new_id = users.add(user)
            print("Created user with ID:", new_id)
            # user_id = users.add(user)
            # user.user_id = user_id

            user = users.get_by_email(dto.requester_email)
            if not user or not new_id:
                raise ValueError("Failed to create or retrieve user")
            user_id = new_id
        else:
            user_id = user.user_id

        if not user_id:
            raise ValueError("Failed to resolve requester_id")

        # 2) Insert ticket with a valid requester_id
        ticket = Ticket(ticket_id=None, requester_id=user_id, subject=dto.subject)
        ticket_id = tickets.add(ticket)

        # 3) First message
        msg = TicketMessage(message_id=None, ticket_id=ticket_id, author_id=user_id, body=dto.body)
        messages.add(msg)

        # Optional: classify on create
        cls = self.llm.classify(dto.subject, dto.body)
        # update category/priority if you want (left out for brevity)

        return ticket_id

    def view_ticket(self, conn, ticket_id:int) -> TicketViewDTO:
        tickets = TicketRepository(conn)
        messages = MessageRepository(conn)
        t = tickets.get(ticket_id)
        if not t:
            raise ValueError("Ticket not found")
        msgs = messages.list_by_ticket(ticket_id)
        return TicketViewDTO(
            ticket_id=t.ticket_id, subject=t.subject, status=t.status.value,
            category=t.category, priority=t.priority.value if t.priority else None,
            llm_summary=t.llm_summary, messages=[m.body for m in msgs]
        )

    def summarize_ticket(self, conn, ticket_id:int):
        tickets = TicketRepository(conn)
        messages = MessageRepository(conn)
        msgs = messages.list_by_ticket(ticket_id)
        if msgs[0].body is not None:
            msg = msgs[0].body
            thread_text = msg #"\n\n".join(m for m in msg)
            summary = self.llm.summarize(thread_text)
            tickets.update_summary(ticket_id, summary)
            return msg, summary
        else:
            return msgs, "No messages to summarize."