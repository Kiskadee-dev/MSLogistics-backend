from peewee import MySQLDatabase
from typing import Optional, Callable
from os import getenv


class Database:
    _db: Optional[MySQLDatabase] = None

    @classmethod
    def get(cls) -> MySQLDatabase:
        """
        Singleton that creates or get a new db object
        """
        if cls._db:
            return cls._db
        cls._db = MySQLDatabase(
            database=getenv("MYSQL_DATABASE"),
            user=getenv("MYSQL_USER"),
            password=getenv("MYSQL_PASSWORD"),
            host=getenv("DB_ADDR", "mariadb"),
        )
        return cls._db

    @classmethod
    def autoclose(cls) -> Callable:
        def decorator(function: Callable):
            def wrapper(*args, **kwargs):
                db = cls.get()
                db.connect()
                try:
                    result = function()
                finally:
                    db.close()
                return result

            return wrapper

        return decorator
