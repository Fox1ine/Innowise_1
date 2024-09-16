from datetime import time
from os import times

from psycopg2 import connect

from BaseManager import BaseManager
from DataBase import DataBase
from RoomsManager import RoomsManager
from Selector import Selector
from StudentsManager import StudentsManager
from DataLoader import DataLoader
from ToJson import ToJson
from ToXML import ToXML


def main():

    db = DataBase()
    db.connect()


    if db.get_connection():

        rooms_manager = RoomsManager(db)
        students_manager = StudentsManager(db)
        selector = Selector()
        to_json = ToJson()
        to_xml = ToXML()

        rooms_manager.create_table()
        students_manager.create_table()

        # region Loading data

        dataloader = DataLoader(rooms_manager, students_manager)

        dataloader.load_data_from_rooms_file('data/rooms.json')
        db.commit()
        dataloader.load_data_from_students_file('data/students.json')
        db.commit()
        # endregion



        #region: selector
        getting_rooms_with_st_count_data, getting_rooms_with_st_count_columns = selector.get_rooms_with_student_count()
        getting_five_rooms_with_min_avg_age_data, getting_five_rooms_with_min_avg_age_columns = selector.get_avg_min_age_in_room()
        getting_rooms_with_max_age_diff_data,getting_rooms_with_max_age_diff_columns = selector.get_max_age_diff_room()
        getting_mixed_sex_rooms_data,getting_mixed_sex_rooms_columns = selector.get_mixedsex_rooms()
        #endregion

        #region: load data to .json
        to_json.json_saver(getting_rooms_with_st_count_columns,getting_rooms_with_st_count_data, 'getting_rooms_with_st_count.json')
        to_json.json_saver(getting_five_rooms_with_min_avg_age_columns,getting_five_rooms_with_min_avg_age_data, 'getting_five_rooms_with_min_avg_age.json')
        to_json.json_saver(getting_rooms_with_max_age_diff_columns,getting_rooms_with_max_age_diff_data, 'getting_rooms_with_max_age_diff.json')
        to_json.json_saver(getting_mixed_sex_rooms_columns,getting_mixed_sex_rooms_data,'getting_mixed_sex_rooms.json')
        #endregion

        #region: load to .xml
        to_xml.xml_saver( getting_rooms_with_st_count_data, getting_rooms_with_st_count_columns, 'getting_rooms_with_st_count.xml')
        to_xml.xml_saver(getting_five_rooms_with_min_avg_age_data, getting_five_rooms_with_min_avg_age_columns, 'getting_five_rooms_with_min_avg_age.xml')
        to_xml.xml_saver(getting_rooms_with_max_age_diff_data,getting_rooms_with_max_age_diff_columns, 'getting_rooms_with_max_age_diff.xml')
        to_xml.xml_saver(getting_mixed_sex_rooms_data,getting_mixed_sex_rooms_columns,'getting_mixed_sex_rooms.xml')
        #endregion

        # Close the connection
        db.disconnect()

if __name__ == '__main__':
    main()
