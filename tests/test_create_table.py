import unittest
from unittest.mock import MagicMock
from src.database import Database
from src.base_manager import BaseManager
from src.queries import q_fot_table_test


class TestCreateTable(unittest.TestCase):
    def setUp(self):
        self.db = MagicMock(spec=Database)
        self.base_manager = BaseManager(self.db)


    def test_create_table(self):

        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        self.db.get_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor


        test_create_table_query = q_fot_table_test

        self.base_manager.create_table(test_create_table_query)

        self.db.get_connection.assert_called_once()
        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(test_create_table_query)

        mock_connection.commit.assert_called_once()

        mock_cursor.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()


