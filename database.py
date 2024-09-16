from peewee import MySQLDatabase
from typing import Optional, Callable
from os import getenv


class Database:
    _db: Optional[MySQLDatabase] = None

    @classmethod
    def get(cls, testing: bool = False) -> MySQLDatabase:
        """
        Singleton that creates or get a new db object
        """
        if cls._db:
            return cls._db
        cls._db = MySQLDatabase(
            database=getenv("MYSQL_DATABASE") if not testing else "TESTING",
            user=getenv("MYSQL_USER"),
            password=getenv("MYSQL_PASSWORD"),
            host=getenv("DB_ADDR", "mariadb"),
        )
        return cls._db
