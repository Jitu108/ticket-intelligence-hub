# application/notifications.py
from abc import ABC, abstractmethod

class TicketEventObserver(ABC):
    @abstractmethod
    def on_created(self, ticket_id:int): ...
    @abstractmethod
    def on_updated(self, ticket_id:int): ...

class EmailNotifier(TicketEventObserver):
    def on_created(self, ticket_id:int): pass
    def on_updated(self, ticket_id:int): pass