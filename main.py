from datetime import time
from os import times

from DataBase import DataBase
from RoomsManager import RoomsManager
from StudentsManager import StudentsManager
from DataLoader import DataLoader


def main():
    # Создаем экземпляр базы данных
    db = DataBase()
    db.connect()

    if db.get_connection():

        rooms_manager = RoomsManager(db)
        students_manager = StudentsManager(db)


        rooms_manager.create_table()
        students_manager.create_table()

        # Загружаем данные
        dataloader = DataLoader(rooms_manager, students_manager)

        # Загружаем данные комнат и выполняем commit
        dataloader.load_data_from_rooms_file('data/rooms.json')
        db.commit()

        # Загружаем данные студентов
        dataloader.load_data_from_students_file('data/students.json')
        db.commit()


        # Закрываем соединение
        db.disconnect()

if __name__ == '__main__':
    main()
