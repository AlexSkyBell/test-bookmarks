from commands.base import Command
from database.base import DatabaseManager


class ListBookmarkCommand(Command):
    def __init__(
        self, db: DatabaseManager, table: str = "bookmarks", order_by="date_added"
    ) -> None:
        super().__init__(db, table)
        self.order_by = order_by

    def execute(self):
        return self.db.read(self.table, order_by=self.order_by)
