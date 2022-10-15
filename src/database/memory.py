from typing import Any, Dict, List, Optional, Union

from database.base import DatabaseManager


class MemoryDatabase(DatabaseManager):
    def open(self):
        self.store = {}

    def close(self):
        self.store = {}

    def create_table(self, table_name: str, columns: Dict):
        self.store[table_name] = []

    def add(self, table_name: str, data: Dict):
        self.store[table_name].append(data)

    def __get_filtered_rows(self, table_name: str, clause: Optional[Dict]):
        def filter_fn(row, filters):
            for key, value in filters.items():
                if row.get(key) and row[key] == value:
                    return row

        filter_ = lambda row: filter_fn(row, clause)
        return list(filter(filter_, self.store[table_name]))

    def read(
        self,
        table_name: str,
        clause: Optional[Dict] = None,
        order_by: Union[Dict, str, None] = None,
    ) -> List[Any]:
        if clause and isinstance(clause, dict):
            res = self.__get_filtered_rows(table_name, clause)
        else:
            res = self.store[table_name]
        if order_by:
            res.sort(key=order_by)

        return res

    def update(self, table_name: str, data: Dict, clause: Optional[Dict] = None):
        if clause and isinstance(clause, dict):
            objs = self.__get_filtered_rows(table_name, clause)
        else:
            objs = self.store[table_name]

        for obj in objs:
            obj.update(data)

    def delete(self, table_name: str, clause: Dict):
        if clause and isinstance(clause, dict):
            to_delete = self.__get_filtered_rows(table_name, clause)
        else:
            to_delete = self.store[table_name]

        self.store[table_name] = [
            obj for obj in self.store[table_name] if obj not in to_delete
        ]
