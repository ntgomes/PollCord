from src.api.api import BackendClient

from requests import Session
from unittest.mock import patch


class MockResponse:
    """
    Class that is used as a fake requests.Response object for the purposes of mocking HTTP
    calls using python-mock. Includes all the functions that are called by api.py so that
    there isn't any TypeError for the mock return.
    """
    def __init__(self, json_data, status_code = 200):
        self.json_data = json_data

    """
    Just returns the JSON body of the response... or the dict representation in Python.
    """
    def json(self):
        return self.json_data


@patch.object(Session, "get")
def test_check_if_poll_exists(mock_get):
    """Given a GET request to /check/<guild_id>/<poll_name>, return and verify the mock JSON"""
    mock_get.return_value = MockResponse({"exists": True})

    test_client = BackendClient()

    result = test_client.check_if_poll_exists(12345, "TEST POLL")
    assert result


@patch.object(Session, "get")
def test_recall_poll(mock_get):
    """Given a GET request to /recall/<guild_id>/<poll_name>, return and verify the mock JSON"""
    mock_get.return_value = MockResponse(
        {
            "guild_id": 12345,
            "poll_name": "MOCK POLL",
            "questions": {
                "question1": {"option1": 23, "option2": 19, "option3": 10},
                "question2": {"option1": 20, "option2": 10},
            },
        }
    )

    test_client = BackendClient()

    result = test_client.recall_poll(12345, "MOCK POLL")
    assert result["guild_id"] == 12345
    assert result["poll_name"] == "MOCK POLL"
    assert len(result["questions"]) == 2


@patch.object(Session, "post")
def test_save_poll_results(mock_get):
    """Given a POST request to /save, return and verify the mock JSON"""
    mock_get.return_value = MockResponse({"success": True})

    test_client = BackendClient()

    result = test_client.save_poll_results(12345, "TEST POLL", {})
    assert result
