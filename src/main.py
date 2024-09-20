from src.database import Database
from src.rooms_manager import RoomsManager
from src.selector import DataSelector
from src.students_manager import StudentsManager
from src.data_loader import DataLoader
from src.json_converter import JsonConverter
from src.xml_converter import XmlConverter
from src.command_handler import CommandLineInterface


def main():
    db = Database()
    db.connect()
    cli = CommandLineInterface(db)
    cli.run()

    if db.get_connection():

        rooms_manager = RoomsManager(db)
        students_manager = StudentsManager(db)
        selector = DataSelector(db)
        to_json = JsonConverter()
        to_xml = XmlConverter()

        rooms_manager.create_table()
        students_manager.create_table()

        # region Loading data

        dataloader = DataLoader(rooms_manager, students_manager)

        dataloader.load_data_from_rooms_file()
        db.commit()
        dataloader.load_data_from_students_file()
        db.commit()
        # endregion

        # region: selector
        getting_rooms_with_st_count_data, getting_rooms_with_st_count_columns = (
            selector.get_rooms_with_student_count()
        )
        (
            getting_five_rooms_with_min_avg_age_data,
            getting_five_rooms_with_min_avg_age_columns,
        ) = selector.get_avg_min_age_in_room()
        (
            getting_rooms_with_max_age_diff_data,
            getting_rooms_with_max_age_diff_columns,
        ) = selector.get_max_age_diff_room()
        getting_mixed_sex_rooms_data, getting_mixed_sex_rooms_columns = (
            selector.get_mixedsex_rooms()
        )
        # endregion

        # region: load data to .json
        to_json.convert_to_json(
            getting_rooms_with_st_count_columns,
            getting_rooms_with_st_count_data,
            "getting_rooms_with_st_count.json",
        )
        to_json.convert_to_json(
            getting_five_rooms_with_min_avg_age_columns,
            getting_five_rooms_with_min_avg_age_data,
            "getting_five_rooms_with_min_avg_age.json",
        )
        to_json.convert_to_json(
            getting_rooms_with_max_age_diff_columns,
            getting_rooms_with_max_age_diff_data,
            "getting_rooms_with_max_age_diff.json",
        )
        to_json.convert_to_json(
            getting_mixed_sex_rooms_columns,
            getting_mixed_sex_rooms_data,
            "getting_mixed_sex_rooms.json",
        )
        # endregion

        # region: load to .xml
        to_xml.convert_to_xml(
            getting_rooms_with_st_count_data,
            getting_rooms_with_st_count_columns,
            "getting_rooms_with_st_count.xml",
        )
        to_xml.convert_to_xml(
            getting_five_rooms_with_min_avg_age_data,
            getting_five_rooms_with_min_avg_age_columns,
            "getting_five_rooms_with_min_avg_age.xml",
        )
        to_xml.convert_to_xml(
            getting_rooms_with_max_age_diff_data,
            getting_rooms_with_max_age_diff_columns,
            "getting_rooms_with_max_age_diff.xml",
        )
        to_xml.convert_to_xml(
            getting_mixed_sex_rooms_data,
            getting_mixed_sex_rooms_columns,
            "getting_mixed_sex_rooms.xml",
        )
        # endregion

        # Close the connection
        db.disconnect()


if __name__ == "__main__":
    main()
