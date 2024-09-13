import psycopg2
from psycopg2 import sql
from Credentials import DB_CONFIG, logger


class DataBase:
    def __init__(self):
        self.connection = None
        self.db_config = DB_CONFIG

    def connect(self):
        """Устанавливает соединение с базой данных."""
        try:
            self.connection = psycopg2.connect(**self.db_config)
            logger.info("Connected to Database")
        except psycopg2.Error as e:
            logger.error(f"Database connection error: {e}")

    def disconnect(self):
        """Закрывает соединение с базой данных."""
        if self.connection:
            self.connection.close()
            logger.info("Connection closed")

    def get_connection(self):
        """Возвращает текущее соединение с базой данных."""
        return self.connection

    def commit(self):
        if self.connection:
            self.connection.commit()
        logger.info("Database commited")
