import sqlite3
from typing import Any, Dict, List, Optional, Union

from database.base import DatabaseManager


class SqliteDatabase(DatabaseManager):
    def open(self):
        self.connection = sqlite3.connect(self.credentials["path"])

    def close(self):
        self.connection.close()

    def _execute(self, statement: str, values: Optional[List] = None) -> sqlite3.Cursor:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def create_table(self, table_name: str, columns: Dict):
        columns_with_types = [
            f"{column} {data_type}" for column, data_type in columns.items()
        ]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            """
        )

    def add(self, table_name: str, data: Dict):
        placeholders = ", ".join("?" * len(data))
        columns = ", ".join(data.keys())
        self._execute(
            f"""
            INSERT INTO {table_name} ({columns}) VALUES ({placeholders})
            """,
            list(data.values()),
        )

    def read(
        self,
        table_name: str,
        clause: Optional[Dict] = None,
        order_by: Union[Dict, str, None] = None,
    ) -> List[Any]:
        query = f"SELECT * FROM {table_name}"
        values = []
        if clause and isinstance(clause, dict):
            placeholders = [f"{column} = ?" for column in clause.keys()]
            where_clause = " AND ".join(placeholders)
            query += f" WHERE {where_clause}"
            values = list(clause.values())

        if order_by:
            query += f" ORDER BY {order_by}"

        return self._execute(query, values)

    def update(self, table_name: str, data: Dict, clause: Optional[Dict] = None):
        placeholders = [f"{column} = ?" for column in data.keys()]
        update = ", ".join(placeholders)
        values = list(clause.values())
        query = f"UPDATE {table_name} SET {update}"
        if clause and isinstance(clause, dict):
            placeholders = []
            for column, value in clause.items():
                placeholders.append(f"{column} = ?")
                values.append(value)
            where_clause = " AND ".join(placeholders)
            query += f" WHERE {where_clause}"
        self._execute(query, values)

    def delete(self, table_name: str, clause: Dict):
        placeholders = [f"{column} = ?" for column in clause.keys()]
        delete_clause = " AND ".join(placeholders)
        self._execute(
            f"""
            DELETE FROM {table_name} WHERE {delete_clause}
            """,
            list(clause.values()),
        )
