import json

from Credentials import logger
from Selector import Selector
from typing import List, Dict, Any

class ToJson:

    """
    A class to handle conversion to data to json format and save it to a file
    """
    def __init__(self):
        """
        Initializes the ToJson class
        """
        pass


    def json_saver(self, columns:List[str], data:List[tuple], file_name):
        """
          Converts data into a list of dictionaries and saves it to a JSON file.

          Args:
              columns: A list of column names corresponding to the data.
              data: A list of tuples, where each tuple represents a row of data.
              file_name: The name of the file where the JSON data will be saved.
          """
        try:
            """Converts data into a list of dictionaries."""
            formatted_data = [{columns[i]: row[i] for i in range(len(columns))} for row in data]
            logger.info("Data converted to a list of dictionaries successfully.")

            with open(file_name, 'w') as json_file:
                json.dump(formatted_data, json_file, indent=4)
            logger.info(f"Data successfully saved to {file_name}")

        except Exception as e:
            logger.error(f"Something went wrong while saving data to {file_name}: {e}")



