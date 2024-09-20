import json
import unittest
from src.data_loader import DataLoader
from unittest.mock import MagicMock, patch, mock_open
import os
from config.config import INITIAL_DATA_DIR
import psycopg2



class TestDataLoadFromFiles(unittest.TestCase):

    def setUp(self):
        self.rooms_manager = MagicMock()
        self.students_manager = MagicMock()
        self.loader = DataLoader(self.rooms_manager, self.students_manager)

    def test_load_data_from_rooms(self):

        mock_data = [{"id": 133, "name": "Room #213"}]
        mock_json = json.dumps(mock_data)

        with patch('builtins.open', mock_open(read_data=mock_json)):
            self.loader.load_data_from_rooms_file()
            self.rooms_manager.add_data.assert_called_once_with(mock_data)

            args, _ = self.rooms_manager.add_data.call_args
            self.assertIsInstance(args[0], list)
            self.assertEqual(args[0], mock_data)
            self.assertIsInstance(args[0][0], dict)
            print(args[0][0])

    def test_load_data_from_students(self):
        mock_data = [{
        "birthday": "2004-01-07T00:00:00.000000",
        "id": 1,
        "name": "Christian Bush",
        "room": 743,
        "sex": "M"
    }]
        mock_json = json.dumps(mock_data)
        with patch('builtins.open', mock_open(read_data=mock_json)):
            self.loader.load_data_from_students_file()
            self.students_manager.add_data.assert_called_once_with(mock_data)

            args, _ = self.students_manager.add_data.call_args
            self.assertIsInstance(args[0], list)
            print(f"{args[0][0]}")
            self.assertEqual(args[0], mock_data)
            self.assertIsInstance(args[0][0], dict)


if __name__ == '__main__':
    unittest.main()


