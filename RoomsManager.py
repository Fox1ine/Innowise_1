import Queries
from BaseManager import BaseManager
from Credentials import logger
from typing import Any, List, Dict

class RoomsManager(BaseManager):
    """
    A manager class for handling operations related to the 'rooms' table.
    """

    def __init__(self, db: Any) -> None:
        """
        Initializes the RoomsManager with a database connection.

        Args:
            db: The database connection object.
        """
        super().__init__(db)

    def create_table(self) -> None:
        """
        Creates the 'rooms' table in the database using a predefined SQL query.
        """
        create_rooms_table_query = Queries.q_create_rooms_table
        super().create_table(create_rooms_table_query)
        logger.info('Rooms table created successfully')

    def drop_table(self) -> None:
        """
        Drops the 'rooms' table from the database using a predefined SQL query.
        """
        drop_table_query = Queries.q_drop_table_room
        super().drop_table(drop_table_query)
        logger.info('Rooms table dropped successfully')

    def add_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Adds room data to the 'rooms' table.

        Args:
            data: A list of dictionaries, each representing a room's data.
        """
        formatted_data = []
        add_data_query = Queries.q_add_data_room
        try:
            # Formatting the data for SQL insertion
            for i in data:
                row_tuple = (i['id'], i['name'])
                formatted_data.append(row_tuple)
            super().add_data(add_data_query, formatted_data)
            logger.info("Rooms data added successfully.")
        except Exception as e:
            logger.error(f"Failed to add data to rooms due to: {e}")
