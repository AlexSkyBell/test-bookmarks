from typing import Dict

from commands.base import Command
from database.base import DatabaseManager


class DeleteCommand(Command):
    def __init__(
        self, data: Dict, db: DatabaseManager, table: str = "bookmarks"
    ) -> None:
        super().__init__(db, table)
        self.data = data

    def execute(self, *args, **kwargs):
        self.db.delete(self.table, self.data)
