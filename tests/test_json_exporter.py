import shutil
import unittest
import os
import json
from src.json_converter import JsonConverter
from config import config
from config.config import TEST_OUTPUT_PATH_DIR, OUTPUT_PATH_DIR
from unittest import mock


class TestExportToJson(unittest.TestCase):

    def setUp(self):
        self.columns = ["name", "age"]
        self.data = [("John", 22), ("Jane", 21)]
        self.json_file_name = "test_output.json"
        self.output_directory = TEST_OUTPUT_PATH_DIR
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def test_json_saver(self):
        json_file_path = os.path.join(self.output_directory, self.json_file_name)
        print(f"Saving JSON file to: {json_file_path}")

        with mock.patch("config.config.OUTPUT_PATH_DIR", config.TEST_OUTPUT_PATH_DIR):
            json_converter = JsonConverter()
            json_converter.convert_to_json(self.columns, self.data, self.json_file_name)

        self.assertTrue(os.path.exists(json_file_path), f"File {json_file_path} was not created")

        with open(json_file_path, "r") as json_file:
            saved_data = json.load(json_file)
            expected_data = [
                {"name": "John", "age": 22},
                {"name": "Jane", "age": 21}
            ]
            self.assertEqual(saved_data, expected_data)

    def tearDown(self):

        json_file_path = os.path.join(self.output_directory, self.json_file_name)
        if os.path.exists(json_file_path):
            os.remove(json_file_path)

        if os.path.exists(self.output_directory):
            try:
                shutil.rmtree(self.output_directory)
            except PermissionError as e:
                print(f"Error removing directory: {e}")


if __name__ == '__main__':
    unittest.main()
