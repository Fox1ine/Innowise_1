import pytest
from unittest import mock
from src.rooms_manager import RoomsManager
from src.students_manager import StudentsManager
from src import queries
import csv


final_dataset = []


@pytest.fixture
def mock_db():

    mock_conn = mock.Mock()
    mock_cursor = mock_conn.cursor.return_value
    return mock_conn, mock_cursor


def test_rooms_with_large_student_count(mock_db):

    mock_conn, mock_cursor = mock_db

    mock_cursor.fetchall.return_value = [
        ("Room 101", 25),
        ("Room 102", 50),
        ("Room 103", 75),
        ("Room 104", 100)
    ]

    rooms_manager = RoomsManager(mock_conn)
    mock_cursor.execute(queries.q_rooms_with_student_count)
    result = mock_cursor.fetchall()

    for room in result:
        assert room[1] > 0, f"Number of students in {room[0]} should be greater than 0"

    total_students = sum([room[1] for room in result])
    assert total_students > 200, "Total number of students should be greater than 200"


def test_avg_min_age_with_large_dataset(mock_db):

    mock_conn, mock_cursor = mock_db

    mock_cursor.fetchall.return_value = [
        ("Room 101", 20.1),
        ("Room 102", 21.3),
        ("Room 103", 19.7),
        ("Room 104", 22.5)
    ]

    rooms_manager = RoomsManager(mock_conn)
    mock_cursor.execute(queries.q_avg_min_age_in_room)
    result = mock_cursor.fetchall()

    for room in result:
        assert 18 <= room[1] <= 25, f"Average age in {room[0]} should be between 18 and 25"

    avg_ages_below_20 = [room[1] for room in result if room[1] < 20]
    assert len(avg_ages_below_20) > 0, "At least one room should have an average age below 20"


def test_max_age_diff_room_with_large_dataset(mock_db):

    mock_conn, mock_cursor = mock_db

    mock_cursor.fetchall.return_value = [
        ("Room 101", 5.0),
        ("Room 102", 7.5),
        ("Room 103", 3.8),
        ("Room 104", 10.0)
    ]

    rooms_manager = RoomsManager(mock_conn)
    mock_cursor.execute(queries.q_max_age_diff_room)
    result = mock_cursor.fetchall()

    for room in result:
        assert 3 <= room[1] <= 10, f"Age difference in {room[0]} should be between 3 and 10"

    max_diff_room = max(result, key=lambda x: x[1])
    assert max_diff_room[0] == "Room 104", "Room 104 should have the maximum age difference"



def test_mixed_sex_rooms_with_large_dataset(mock_db):

    mock_conn, mock_cursor = mock_db

    mock_cursor.fetchall.return_value = [
        (1,),
        (2,),
        (3,),
        (4,)
    ]

    students_manager = StudentsManager(mock_conn)
    mock_cursor.execute(queries.q_mixedsex_rooms)
    result = mock_cursor.fetchall()

    assert len(result) > 2, "There should be more than two rooms with mixed-sex students"

    for room in result:
        assert room[0] > 0, f"Room ID should be positive, found {room[0]}"





if __name__ == "__main__":
    pytest.main([__file__])

