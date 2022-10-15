from abc import abstractstaticmethod
from typing import Any, Dict, List, Optional, Union

from requests import delete


class DatabaseManager:
    def __init__(self, credentials: Optional[Dict] = None) -> None:
        self.credentials = credentials
        self.open()

    def __del__(self):
        self.close()

    @abstractstaticmethod
    def open(self):
        pass

    @abstractstaticmethod
    def close(self):
        pass

    @abstractstaticmethod
    def _execute(self, statement: str, values: List) -> Any:
        pass

    @abstractstaticmethod
    def create_table(self, table_name: str, columns: Dict):
        pass

    @abstractstaticmethod
    def add(self, table_name: str, data: Dict):
        pass

    @abstractstaticmethod
    def read(
        self,
        table_name: str,
        clause: Optional[Dict] = None,
        order_by: Union[Dict, str, None] = None,
    ) -> List[Any]:
        pass

    @abstractstaticmethod
    def update(self, table_name: str, data: Dict, clause: Optional[Dict] = None):
        pass

    @abstractstaticmethod
    def delete(self, table_name: str, clause: Dict):
        pass
