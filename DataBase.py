import psycopg2
from psycopg2 import sql
from typing import Optional
from Credentials import DB_CONFIG, logger

class DataBase:
    """
    A class to manage the database connection.
    """

    def __init__(self) -> None:
        """
        Initializes the DataBase object and connects to the database.
        """
        self.connection: Optional[psycopg2.extensions.connection] = None
        self.db_config: dict = DB_CONFIG
        self.connect()

    def connect(self) -> None:
        """
        Establishes a connection to the database.
        """
        try:
            self.connection = psycopg2.connect(**self.db_config)
            logger.info("Connected to Database")
        except psycopg2.Error as e:
            logger.error(f"Database connection error: {e}")

    def disconnect(self) -> None:
        """
        Closes the connection to the database.
        """
        if self.connection:
            self.connection.close()
            logger.info("Connection closed")

    def get_connection(self) -> Optional[psycopg2.extensions.connection]:
        """
        Returns the current connection to the database.
        """
        return self.connection

    def commit(self) -> None:
        """
        Commits the current transaction.
        """
        if self.connection:
            self.connection.commit()
            logger.info("Database committed")
