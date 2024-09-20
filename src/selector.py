import queries
from typing import Tuple, List, Any

from config.config import logger


class DataSelector:
    """
    A selector class for performing various data retrieval operations from the database.
    Inherits from the DataBase class.
    """

    def __init__(self, db) -> None:
        """
        Initializes the Selector by establishing a connection to the database.
        """
        self.db = db

    def get_rooms_with_student_count(self) -> Tuple[List[Tuple[Any, ...]], List[str]]:
        """
        Retrieves the count of students in each room from the database.

        Returns:
            A tuple containing:
            - data: A list of tuples, each representing a row of data.
            - columns: A list of column names.
        """
        with self.db.get_connection().cursor() as cursor:
            cursor.execute(queries.q_rooms_with_student_count)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
            logger.info("get_rooms_with_student_count worked successfully.")
            return data, columns

    def get_avg_min_age_in_room(self) -> Tuple[List[Tuple[Any, ...]], List[str]]:
        """
        Retrieves the average and minimum age of students in each room from the database.

        Returns:
            A tuple containing:
            - data: A list of tuples, each representing a row of data.
            - columns: A list of column names.
        """
        with self.db.get_connection().cursor() as cursor:
            cursor.execute(queries.q_avg_min_age_in_room)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
            logger.info("get_avg_min_age_in_room worked successfully.")
            return data, columns

    def get_max_age_diff_room(self) -> Tuple[List[Tuple[Any, ...]], List[str]]:
        """
        Retrieves the maximum age difference among students in each room from the database.

        Returns:
            A tuple containing:
            - data: A list of tuples, each representing a row of data.
            - columns: A list of column names.
        """
        with self.db.get_connection().cursor() as cursor:
            cursor.execute(queries.q_max_age_diff_room)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
            logger.info("get_max_age_diff_room worked successfully.")
            return data, columns

    def get_mixedsex_rooms(self) -> Tuple[List[Tuple[Any, ...]], List[str]]:
        """
        Retrieves the rooms with a mix of male and female students from the database.

        Returns:
            A tuple containing:
            - data: A list of tuples, each representing a row of data.
            - columns: A list of column names.
        """
        with self.db.get_connection().cursor() as cursor:
            cursor.execute(queries.q_mixedsex_rooms)
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
            logger.info("get_mixedsex_rooms worked successfully.")
            return data, columns
