#infrastructure/db.py
import pyodbc
from contextlib import contextmanager
from typing import Generator
from ..config import settings

class DbConnectionProvider:
    def __init__(self, conn_str: str):
        self.conn_str = conn_str

    def connect(self):
        return pyodbc.connect(self.conn_str, autocommit=False)
    
class UnitOfWork:
    def __init__(self, provider: DbConnectionProvider):
        self.provider = provider
        self.connection = None
    def __enter__(self):
        self.conn = self.provider.connect()
        return self.conn
    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
        