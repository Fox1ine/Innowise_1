import unittest
from unittest.mock import MagicMock, patch

from src.database import Database


class TestDatabase(unittest.TestCase):


    @patch('psycopg2.connect')
    def test_database_connection_success(self, mock_connect):

        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        db = Database()

        mock_connect.assert_called_once()
        mock_db = db.get_connection()
        self.assertIsNotNone(mock_db)

        self.assertEqual(mock_connect.call_count, 1)


    @patch('psycopg2.connect')
    def test_database_commit(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        db = Database()

        db.commit()
        mock_conn.commit.assert_called_once()


    @patch('psycopg2.connect')
    def test_database_disconnect(self, mock_connect):
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn

        db = Database()


        db.disconnect()

        mock_conn.close.assert_called_once()





