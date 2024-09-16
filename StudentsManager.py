from BaseManager import BaseManager
from Credentials import *
import Queries
from typing import List, Dict, Any


class StudentsManager(BaseManager):
    """
    Manager class for handling operations related to the 'students' table.
    Inherits from BaseManager.
    """

    def __init__(self, db: Any) -> None:
        """
        Initializes the StudentsManager with a database connection.

        Args:
            db: The database connection object.
        """
        super().__init__(db)

    def create_table(self) -> None:
        """
        Creates the 'students' table in the database and sets up necessary indexes.
        """
        create_student_table_query = Queries.q_create_student_table
        super().create_table(create_student_table_query)
        logger.info("Table 'students' created successfully")
        super().create_indexes()

    def drop_table(self) -> None:
        """
        Drops the 'students' table from the database.
        """
        drop_student_table_query = Queries.q_drop_student_table_query
        super().drop_table(drop_student_table_query)
        logger.info('Table "students" dropped successfully')

    def add_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Adds multiple student records to the 'students' table in the database.

        Args:
            data: A list of dictionaries, where each dictionary contains student information.
        """
        formatted_data = []
        add_data_query = Queries.q_add_data_query

        for i in data:
            row_tuple = (i['id'], i['name'], i['birthday'], i['sex'], i['room'])
            formatted_data.append(row_tuple)

        super().add_data(add_data_query, formatted_data)
        logger.info("Students data added successfully.")
