import unittest
from unittest.mock import MagicMock
from src.database import Database
from src.base_manager import BaseManager
from src.queries import q_for_test


class TestExecuteQuery(unittest.TestCase):

    def setUp(self):
        self.db = MagicMock(spec=Database)
        self.base_manager = BaseManager(self.db)



    def test_execute_query_success(self):

        mock_connection = MagicMock()
        mock_cursor = MagicMock()

        self.db.get_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        expected_data = [("Pavel", 25), ("BOBA", 30)]
        mock_cursor.fetchall.return_value = expected_data

        test_query = q_for_test
        self.base_manager.execute_query(test_query)
        self.db.get_connection.assert_called_once()

        mock_connection.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(test_query, None)
        mock_connection.commit.assert_called_once()

        result = mock_cursor.fetchall()
        print(result)
        self.assertEqual(result, expected_data)
        mock_cursor.close.assert_called_once()



if __name__ == '__main__':
    unittest.main()
