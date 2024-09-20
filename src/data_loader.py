import json
from typing import Any

from config.config import *


class DataLoader:
    """
    A class for loading data into the database from JSON files.
    """

    def __init__(self, rooms_manager, students_manager) -> None:
        """
        Initializes the DataLoader with managers for rooms and students.

        Args:
            rooms_manager: The manager responsible for handling room data.
            students_manager: The manager responsible for handling student data.
        """
        self.rooms_manager = rooms_manager
        self.students_manager = students_manager

    def load_data_from_rooms_file(self) -> None:
        """
        Loads room data from a JSON file and inserts it into the database.

        Args:
            rooms_file_path: The path to the JSON file containing room data.
        """
        data_room_path = os.path.join(INITIAL_DATA_DIR,'rooms.json')
        with open(data_room_path, "r", encoding="utf-8") as rooms_file:
            rooms_data = json.load(rooms_file)
            self.rooms_manager.add_data(rooms_data)
            logger.info(f"Data loaded successfully ")

    def load_data_from_students_file(self) -> None:
        """
        Loads student data from a JSON file and inserts it into the database.

        Args:
            students_file_path: The path to the JSON file containing student data.
        """

        data_student_path = os.path.join(INITIAL_DATA_DIR, 'students.json')
        with open(data_student_path, "r", encoding="utf-8") as students_file:
            students_data = json.load(students_file)
            self.students_manager.add_data(students_data)
            logger.info(f"Data loaded successfully ")
