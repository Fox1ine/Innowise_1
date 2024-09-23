import argparse
import argparse
from config.config import *

from src.data_loader import DataLoader
from src.database import Database
from src.json_converter import JsonConverter
from src.xml_converter import XmlConverter
from src.rooms_manager import RoomsManager
from src.students_manager import StudentsManager


class CommandLineInterface:

    def __init__(self,db):
        self.parser = argparse.ArgumentParser(description="Program for loading data, executing queries and outputting data in json and xml")
        self.db = db
        self.setup_arguments()

    def setup_arguments(self):
        self.parser.add_argument("--file-path", type=str, help="Path to file (for example  .json or .csv)", default="./data/room.json")
        self.parser.add_argument("--query", type=str, help="Sql query to execute", default="SELECT * FROM rooms")
        self.parser.add_argument("--create-tables", action="store_true", help="Create tables for rooms and students", default=False)
        self.parser.add_argument("--drop-tables", action="store_true", help="Drop tables for rooms and students", default=False)
        self.parser.add_argument("--table", type=str, choices=["rooms", "students"], help="Choose which table to work on", default="rooms")



    def parse_arguments(self):
        return self.parser.parse_args()


    def run(self):
        args = self.parse_arguments()

        print("ARGS:", args)

        rooms_manager = RoomsManager(self.db)
        students_manager = StudentsManager(self.db)
        data_loader = DataLoader(rooms_manager, students_manager)

        try:
            if args.create_tables:
                if args.table == "rooms":
                    print("Creating rooms table.......")
                    rooms_manager.create_table()
                elif args.table == "students":
                 print("Creating students table.......")
            students_manager.create_table()
        except Exception as e:
            print(f"Something went wrong with creating table: {e}")

        try:
            if args.drop_tables:
                if args.table == "rooms":
                    print("Dropping rooms table.......")
                    rooms_manager.drop_table()
                elif args.table == "students":
                    print("Dropping students table.......")
                    students_manager.drop_table()
        except Exception as e:
            print(f"Something went wrong with dropping table: {e}")


        try:
            if args.table == "rooms":
                print(f"Loading rooms data from file: {args.file_path}")
                data_loader.load_data_from_rooms_file()
            elif args.table == "students":
                print(f"Loading students data from file: {args.file_path}")
                data_loader.load_data_from_students_file()
        except Exception as e:
            print(f"Something went wrong with loading data from file: {e}")


        try:
            if args.query:
                print(f"Querying the database: {args.query}")
                result = self.db.execute_query(args.query)
                print(result)

        except Exception as e:
            print(f"Something went wrong with querying the database: {e}")







