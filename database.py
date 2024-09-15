from peewee import MySQLDatabase
from typing import Optional
from os import getenv


class Database:
    """
    Singleton that creates or get a new db object
    """

    db: Optional[MySQLDatabase] = None

    @classmethod
    def get(cls) -> MySQLDatabase:
        if cls.db:
            return cls.db
        cls.db = MySQLDatabase(
            database="Estoque", user="", password="", host=getenv("db_addr", "mariadb")
        )
        return cls.db
