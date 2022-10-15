from typing import Dict, Optional

from commands.base import Command
from database.base import DatabaseManager


class UpdateCommand(Command):
    def __init__(
        self,
        data: Dict,
        db: DatabaseManager,
        table: str = "bookmarks",
        clause: Optional[Dict] = None,
    ) -> None:
        super().__init__(db, table)
        self.data = data
        self.clause = clause

    def execute(self):
        self.db.update(self.table, self.data, self.clause)
