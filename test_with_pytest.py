import pytest
import requests


def test_always_pass():
    assert True


@pytest.mark.xfail
def test_always_fail():
    assert False


def test_capitalize():
    assert "daniel".capitalize() == "Daniel"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }


# Fixtures: Managing state and dependencies
# You can put the repeated data (peoples list) into a single function decorated with @pytest.fixture to indicate the function is a pytest fixture
# Arrange
@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def format_data_for_display(people):
    people_list = []
    for person in people:
        people_list.append(
            f"{person['given_name']} {person['family_name']} {person['title']}"
        )
    return people_list


def test_format_data_for_display(example_people_data):
    # Act
    fmt_data = format_data_for_display(example_people_data)
    # Assert
    assert fmt_data == [
        "Alfonsa Ruiz Senior Software Engineer",
        "Sayid Khan Project Manager",
    ]


def format_data_for_excel(people):
    # implement this!
    # r = requests.get("https://google.com") this should raise a runtime error from the autouse fixture
    return """given,family,title"""


def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title"""


def get_my_ip():
    response = requests.get("http://ipinfo.io/json")
    return response.json()["ip"]


def test_get_my_ip(monkeypatch):
    # Automated tests should be fast, isolated/independent, and deterministic/repeatable.
    # Thus if you need to test code that makes an external HTTP request to a third-party API
    # you should mock the request
    my_ip = "123.123.123.123"

    class MockResponse:
        def __init__(self, json_body):
            self.json_body = json_body

        def json(self):
            return self.json_body

    monkeypatch.setattr(
        requests, "get", lambda *args, **kwargs: MockResponse({"ip": my_ip})
    )
    assert get_my_ip() == my_ip
