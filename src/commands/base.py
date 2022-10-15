from abc import abstractmethod

from database.base import DatabaseManager


class Command:
    def __init__(self, db: DatabaseManager, table: str = "bookmarks") -> None:
        self.table = table
        self.db = db

    @abstractmethod
    def execute(self):
        pass
