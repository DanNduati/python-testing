import string
from unittest import mock
import pytest
import requests
from requests import Response


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
    response = mock.create_autospec(Response)
    response.json.return_value = {"ip": my_ip}
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: response)
    assert get_my_ip() == my_ip


def is_palindrome(s: str):
    if s.lower().replace(" ", "").translate(
        s.maketrans("", "", string.punctuation)
    ) == s[::-1].lower().replace(" ", "").translate(
        s[::-1].maketrans("", "", string.punctuation)
    ):
        return True
    return False


# Initial set of tests
"""
def test_is_palindrome_empty_string():
    assert is_palindrome("")


def test_is_palindrome_single_character():
    assert is_palindrome("a")


def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")


def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even")


def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?")

def test_is_palindrome_not_palindrome():
    assert not is_palindrome("abc")
    
def test_is_palindrome_not_quite():
    assert not is_palindrome("abab")
"""
# All the above palindrome related tests except the last two have the same shape
# Paremetrize them to single test definitions
# The first argument to parametrize() is a comma-delimited string of parameter names
# The second argument is a list of either tuples or single values that represent the parameter value(s)
"""
@pytest.mark.parametrize("palindrome",[
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)
    
@pytest.mark.parametrize("non_palindrome",[
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)
"""
# Combine all palindrome related tests into one
@pytest.mark.parametrize(
    "maybe_palindrome,expected_result",
    [
        ("", True),
        ("a", True),
        ("Bob", True),
        ("Never odd or even", True),
        ("Do geese see God?", True),
        ("abc", False),
        ("abab", False),
    ],
)
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
