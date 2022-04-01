from .dbconfig import config

import psycopg2


class DatabaseConnection:

    # setting initial params
    def __init__(self, params):
        self.params = params
        self._cursor = None
        self._conn = None

    # connecting at the start of with block
    def __enter__(self):
        self._conn = psycopg2.connect(**self.params)
        self._conn.autocommit = True
        self._cursor = self._conn.cursor()
        return self

    # auto closing at the end of with block
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    # closing cursor and connection
    def close(self):
        self._conn.close()

    # executing string query
    def query(self, query: str):
        self._cursor.execute(query)

    def fetchall(self) -> list[tuple]:
        return self._cursor.fetchall()

    # executing multiple insert query
    def execute_many(self, query: str, insert_list: list):
        self._cursor.executemany(query, insert_list)


# class for database access
class Database:

    # initializing from params
    def __init__(self):
        self._conn = None
        self.params = config()

    # returning connection
    def get_connection(self) -> DatabaseConnection:
        return DatabaseConnection(self.params)
