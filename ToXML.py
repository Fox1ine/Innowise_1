import xml.etree.ElementTree as ET
from Credentials import logger
from typing import List, Any

class ToXML:
    """
    A class to handle conversion of data to XML format and save it to a file.
    """
    def __init__(self)->None:
        """
       Initializes the ToXML class.
       """
        pass

    def xml_saver(self, data: List[tuple], columns:List[str], file_name:str) -> None:
        try:
            formatted_data = [{str(columns[i]): row[i] for i in range(len(columns))} for row in data]
            logger.info("Data converted to a list of dictionaries successfully.")
            root = ET.Element('data')

            # Create sub-elements for each data item
            for item_data in formatted_data:
                item = ET.SubElement(root, 'item')

                # Add sub-elements for each property
                for key, value in item_data.items():
                    property_element = ET.SubElement(item, key)
                    property_element.text = str(value)


            tree = ET.ElementTree(root)
            tree.write(file_name, encoding='utf-8', xml_declaration=True)
            logger.info(f'Data successfully saved to {file_name}')

        except Exception as e:
            logger.error(f'Something went wrong while saving data to {file_name}: {e}')
