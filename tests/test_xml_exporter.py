import os
import shutil
import unittest
import xml.etree.ElementTree as ET

from config import config
from src.xml_converter import XmlConverter


class TestExportToXML(unittest.TestCase):

    def setUp(self):
        self.columns = ["name", "age"]
        self.data = [("Paul", 22), ("Bob", 93)]
        self.xml_file_name = "test_output.xml"
        self.output_directory = config.TEST_OUTPUT_PATH_DIR
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def test_xml_export(self):

        xml_file_path = os.path.join(self.output_directory, self.xml_file_name)
        print(f"Saving XML file to: {xml_file_path}")


        xml_converter = XmlConverter()

        xml_converter.xml_saver(self.data,self.columns, xml_file_path)  # Передаем полный путь

        self.assertTrue(os.path.exists(xml_file_path), f"File {xml_file_path} was not created")


        with open(xml_file_path, "r") as file:
            content = file.read()
            print("XML File Content:\n", content)

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        expected_data = [
            {"name": "Paul", "age": 22},
            {"name": "Bob", "age": 93}
        ]

        for i,item in enumerate(root.findall('item')):
            self.assertEqual(item.find('name').text, expected_data[i]["name"])
            self.assertEqual(item.find('age').text, str(expected_data[i]["age"]))


    def tearDown(self):

        xml_file_path = os.path.join(self.output_directory, self.xml_file_name)
        if os.path.exists(xml_file_path):
            os.remove(xml_file_path)

        if os.path.exists(self.output_directory):
            try:
                shutil.rmtree(self.output_directory)
            except PermissionError as e:
                print(f"Error removing directory: {e}")


if __name__ == '__main__':
    unittest.main()
