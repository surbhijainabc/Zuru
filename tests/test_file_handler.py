import json
import pytest
from unittest.mock import mock_open, patch
from pyls.file_handler import FileHandler


@pytest.fixture
def example_json_data():
    """
    Fixture providing example JSON data for testing.

    :return: Example JSON data
    """
    return {'key': 'value'}


def test_read_json_file(example_json_data):
    """
    Test the read_json_file method of FileHandler class.

    It mocks the open function to simulate reading from a JSON file and asserts that the method returns the
    expected JSON data.

    :param example_json_data: Example JSON data for testing.
    :return: None
    """
    with patch('builtins.open', mock_open(read_data=json.dumps(example_json_data))):
        result = FileHandler.read_json_file('test.json')

    assert result == example_json_data
