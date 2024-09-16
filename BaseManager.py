import Queries
from Credentials import *
from typing import Any, Optional, List, Tuple

class BaseManager:
    """
    Base manager class for handling database operations.
    """

    def __init__(self, db: Any) -> None:
        """
        Initializes the BaseManager with a database connection.

        Args:
            db: The database connection object.
        """
        self.db = db

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> None:
        """
        Executes a generic SQL query with optional parameters.

        Args:
            query: The SQL query to be executed.
            params: Optional parameters for the SQL query.
        """
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            logger.info("Query executed successfully")
        except Exception as e:
            connection.rollback()
            logger.error(f"Query failed due to {e}")
        finally:
            cursor.close()

    def create_table(self, create_table_query: str) -> None:
        """
        Creates a table using the provided SQL query.

        Args:
            create_table_query: The SQL query to create a table.
        """
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
        except Exception as e:
            connection.rollback()
            logger.error(f"Table creation failed due to {e}")
        finally:
            cursor.close()

    def drop_table(self, drop_table_query: str) -> None:
        """
        Drops a table using the provided SQL query.

        Args:
            drop_table_query: The SQL query to drop a table.
        """
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute(drop_table_query)
            connection.commit()
            logger.info("Table dropped successfully")
        except Exception as e:
            connection.rollback()
            logger.error(f"Table drop failed due to {e}")
        finally:
            cursor.close()

    def add_data(self, insert_query: str, data: List[Tuple]) -> None:
        """
        Inserts data into a table using the provided SQL query.

        Args:
            insert_query: The SQL query to insert data.
            data: A list of tuples representing the data to be inserted.
        """
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.executemany(insert_query, data)
            connection.commit()
        except Exception as e:
            connection.rollback()
            logger.error(f"Data insertion failed due to {e}")
        finally:
            cursor.close()

    def create_indexes(self) -> None:
        """
        Creates indexes on the specified columns of the table.
        """
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            cursor.execute(Queries.q_create_index)
            connection.commit()
            logger.info("Indexes created successfully")
        except Exception as e:
            connection.rollback()
            logger.error(f"Index creation failed due to {e}")
        finally:
            cursor.close()
