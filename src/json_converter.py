import json
import os
from config import config
from typing import List


class JsonConverter:
    """
    A class to handle conversion to data to json format and save it to a file
    """

    def __init__(self):
        """
        Initializes the ToJson class
        """
        pass

    def convert_to_json(self, columns: List[str], data: List[tuple], file_name):
        """
        Converts data into a list of dictionaries and saves it to a JSON file.

        Args:
            columns: A list of column names corresponding to the data.
            data: A list of tuples, where each tuple represents a row of data.
            file_name: The name of the file where the JSON data will be saved.
        """
        try:
            """Converts data into a list of dictionaries."""
            file_to_output_directory = os.path.join(config.OUTPUT_PATH_DIR, file_name)
            formatted_data = [
                {columns[i]: row[i] for i in range(len(columns))} for row in data
            ]
            config.logger.info("Data converted to a list of dictionaries successfully.")

            with open(file_to_output_directory, "w") as json_file:
                json.dump(formatted_data, json_file, indent=4)
            config.logger.info(f"Data successfully saved to {file_name}")

        except Exception as e:
            config.logger.error(f"Something went wrong while saving data to {file_name}: {e}")
