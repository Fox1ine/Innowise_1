from BaseManager import BaseManager
from Credentials import *




class RoomsManager(BaseManager):
    def __init__(self, db):
        super().__init__(db)

    def create_table(self):
        create_rooms_table_query = """
        CREATE TABLE IF NOT EXISTS rooms (
            id INT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        """
        super().create_table(create_rooms_table_query)
        logger.info('Rooms table created successfully')

    def drop_table(self):
        drop_table_query = "DROP TABLE IF EXISTS rooms;"
        super().drop_table(drop_table_query)
        logger.info('Rooms table dropped successfully')

    def add_data(self, data):
        formatted_data = []
        add_data_query = "INSERT INTO rooms (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;"

        try:
            for i in data:
                row_tuple = (i['id'], i['name'])
                formatted_data.append(row_tuple)
            super().add_data(add_data_query, formatted_data)
            logger.info("Rooms data added successfully.")
        except Exception as e:
            logger.error(f"Failed to add data to rooms due to: {e}")

