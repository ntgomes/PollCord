"""
This module contains all functions needed to call the backend client
for PollCord to save and fetch polls.
"""

import os
import json
import requests as http

from dotenv import load_dotenv


class BackendClient:
    """
    Client class that be used to make HTTP calls to the backend to save
    and fetch poll information for PollCord.
    """

    def __init__(self):
        """Constructor. Depends on API_HOSTNAME defined in .env file within the root
        frontend folder"""
        load_dotenv()
        self.api_hostname = os.getenv("API_HOSTNAME")
        self.session = http.Session()

        # This is so that the client promises to sends and retrieves in JSON
        self.session.headers.update({"Content-Type": "application/json"})

    def check_if_poll_exists(self, guild_id, poll_name):
        """
        Makes a GET request to /check/<guild_id>/<poll_name> endpoint to see if the
        given guild ID and poll name combination already exist in the backend.

        Args:
          guild_id:  The guild ID to check the existence for
          poll_name: The poll_name to be used to check existence
        Returns:
          bool. True if poll exists; false otherwise
        """
        return self.session.get(
            self.api_hostname + "/check/{0}/{1}".format(guild_id, poll_name)
        ).json()["exists"]

    def save_poll_results(self, guild_id: str, poll_name, result_data):
        """
        Makes a POST request to /save endpoint with given guild ID and poll name,
        and poll result data so that it can be stored in the backend.

        Args:
          guild_id:  The guild ID that is associated with the poll
          poll_name: The poll name that should be saved
          result_data: Poll data that should saved; should be in this dict format:
            {
                "question1": {
                    "question_text": "Maybe the beach today?",
                    "option1": 23,
                    "option2": 19,
                    "option3": 10,
                    ...
                },
                "question2": {
                    "question_text": "How is the course going?",
                    "option1": 20,
                    "option2": 10,
                    ...
                },
                ...
            }
        Returns:
          bool. True if saved successfully; false otherwise
        """
        return self.session.post(
            self.api_hostname + "/save",
            json.dumps(
                {
                    "guild_id": str(guild_id),
                    "poll_name": poll_name,
                    "results": result_data,
                }
            ),
        ).json()["success"]

    def recall_poll(self, guild_id, poll_name):
        """
        Makes a GET request to /recall/<guild_id>/<poll_name> endpoint to see
        if the given guild ID and pollname combination already exist in the backend.

        Args:
          guild_id:  The guild ID that is associated with the poll
          poll_name: The poll name that should be recalled
        Returns:
          dict: Returns the poll information if so, and None otherwise. Looks like the following:
            {
                "guild_id": 12345,
                "pool_name": "MY POLL",
                "results":{
                    "question1": {
                        "question_text": "Maybe the beach today?",
                        "option1": 23,
                        "option2": 19,
                        "option3": 10,
                        ...
                    },
                    "question2": {
                        "question_text": "How is the course going?",
                        "option1": 20,
                        "option2": 10,
                        ...
                    },
                    ...
                }
            }
        """
        return self.session.get(
            self.api_hostname + "/recall/{0}/{1}".format(guild_id, poll_name)
        ).json()
