# application/rules.py
from ..domain.entities import Ticket
from ..domain.value_objects import Priority

def enforce_sane_priority(ticket: Ticket):
    if ticket.priority == Priority.HIGH and (ticket.category or "").lower() == "feature":
        # example rule: features can't be HIGH without approval
        pass