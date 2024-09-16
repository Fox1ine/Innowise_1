import json
from typing import Any

class DataLoader:
    """
    A class for loading data into the database from JSON files.
    """

    def __init__(self, rooms_manager: Any, students_manager: Any) -> None:
        """
        Initializes the DataLoader with managers for rooms and students.

        Args:
            rooms_manager: The manager responsible for handling room data.
            students_manager: The manager responsible for handling student data.
        """
        self.rooms_manager = rooms_manager
        self.students_manager = students_manager

    def load_data_from_rooms_file(self, rooms_file_path: str) -> None:
        """
        Loads room data from a JSON file and inserts it into the database.

        Args:
            rooms_file_path: The path to the JSON file containing room data.
        """
        with open(rooms_file_path, 'r', encoding='utf-8') as rooms_file:
            rooms_data = json.load(rooms_file)
            self.rooms_manager.add_data(rooms_data)

    def load_data_from_students_file(self, students_file_path: str) -> None:
        """
        Loads student data from a JSON file and inserts it into the database.

        Args:
            students_file_path: The path to the JSON file containing student data.
        """
        with open(students_file_path, 'r', encoding='utf-8') as students_file:
            students_data = json.load(students_file)
            self.students_manager.add_data(students_data)
