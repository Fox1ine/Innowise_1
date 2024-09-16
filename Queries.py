

#region: Selects
q_rooms_with_student_count = """
SELECT r.name AS "Room Name", COUNT(s.id) AS "Count of student"
FROM rooms AS r
LEFT JOIN students AS s ON r.id = s.room
GROUP BY r.name
"""


q_avg_min_age_in_room = """
SELECT r.name AS "Room Name", 
AVG(EXTRACT(YEAR FROM AGE(s.birthday)))::FLOAT AS "Average Age"
FROM rooms AS r
JOIN students AS s ON r.id = s.room
GROUP BY r.name
ORDER BY "Average Age" ASC
LIMIT 5;
"""


q_max_age_diff_room ="""
SELECT r.name AS "Room Name", 
(MAX(EXTRACT(YEAR FROM AGE(s.birthday))) - MIN(EXTRACT(YEAR FROM AGE(s.birthday))))::FLOAT AS "Age Diff"
FROM rooms AS r
JOIN students AS s ON r.id = s.room
GROUP BY r.name
ORDER BY "Age Diff" DESC
LIMIT 5;
"""


q_mixedsex_rooms = """
SELECT DISTINCT s.room AS "Room ID"
FROM students AS s
JOIN students s2 ON s.room = s2.room
WHERE s.sex = 'F' AND s2.sex = 'M';
"""

#endregion

#region: Queries for student
q_create_student_table = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    sex CHAR(1) CHECK (sex IN ('M', 'F')),
    room INT,
    FOREIGN KEY(room) REFERENCES rooms(id) ON DELETE CASCADE
);
"""

q_drop_student_table_query = "DROP TABLE IF EXISTS students;"

q_add_data_query  = "INSERT INTO students (id, name, birthday, sex, room) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;"

q_create_index = "CREATE INDEX idx_students_room_sex ON students (room, sex);"
#endregion

#region: Queries for rooms
q_create_rooms_table = """
CREATE TABLE IF NOT EXISTS rooms (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
"""

q_drop_table_room = "DROP TABLE IF EXISTS rooms;"

q_add_data_room = "INSERT INTO rooms (id, name) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;"
#endregion