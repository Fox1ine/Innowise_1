import json

class DataLoader:
    def __init__(self, rooms_manager, students_manager):
        self.rooms_manager = rooms_manager
        self.students_manager = students_manager


    def load_data_from_rooms_file(self, rooms_file_path):
        # Загрузка данных комнат
        with open(rooms_file_path, 'r', encoding='utf-8') as rooms_file:
            rooms_data = json.load(rooms_file)
            self.rooms_manager.add_data(rooms_data)


    def load_data_from_students_file(self, students_file_path):
        # Загрузка данных студентов
        with open(students_file_path, 'r', encoding='utf-8') as students_file:
            students_data = json.load(students_file)
            self.students_manager.add_data(students_data)
