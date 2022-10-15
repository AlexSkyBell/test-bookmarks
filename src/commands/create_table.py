from commands.base import Command


class CreateTableCommand(Command):
    def execute(self):
        self.db.create_table(
            self.table,
            {
                "id": "integer primary key autoincrement",
                "title": "text not null",
                "url": "text not null",
                "notes": "text",
                "date_added": "text not null",
            },
        )
