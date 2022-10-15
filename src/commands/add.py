from datetime import datetime
from typing import Dict

from commands.base import Command
from database.base import DatabaseManager


class AddBookmarkCommand(Command):
    def __init__(
        self, data: Dict, db: DatabaseManager, table: str = "bookmarks"
    ) -> None:
        super().__init__(db, table)
        self.data = data

    def execute(self):
        self.data["date_added"] = datetime.now()
        self.db.add(self.table, self.data)
        return "Bookmark added"
