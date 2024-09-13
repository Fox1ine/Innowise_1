from BaseManager import BaseManager
from Credentials import *


class StudentsManager(BaseManager):
    def __init__(self, db):
        super().__init__(db)

    def create_table(self):
        create_student_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            birthday DATE NOT NULL,
            sex CHAR(1) CHECK (sex IN ('M', 'F')),
            room INT,
            FOREIGN KEY(room) REFERENCES rooms(id) ON DELETE CASCADE
);
        """
        super().create_table(create_student_table_query)
        logger.info("Table students created successfully")

    def drop_table(self):
        drop_student_table_query = 'DROP TABLE IF EXISTS students;'
        super().drop_table(drop_student_table_query)
        logger.info('Table student dropped successfully ')

    def add_data(self, data):
        formatted_data = []
        add_data_query = "INSERT INTO students (id, name, birthday, sex, room) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;"
        for i in data:
            row_tuple = (i['id'], i['name'], i['birthday'], i['sex'], i['room'])
            formatted_data.append(row_tuple)
        super().add_data(add_data_query, formatted_data)
        logger.info("Students data added successfully.")
