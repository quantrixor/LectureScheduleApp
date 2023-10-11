import pytest
import requests


@pytest.fixture
def api_url():
    return "http://127.0.0.1:5000/lectures/"


def test_add_lecture(api_url):
    lecture_data = {
        "title": "Physics 105",
        "lecturer_name": "Dr. Smith",
        "start_time": "10:00",
        "end_time": "11:00",
        "room": "Room 102"
    }

    response = requests.post(api_url, json=lecture_data)

    assert response.status_code == 201
    assert response.json() == {"message": "Lecture created successfully"}
