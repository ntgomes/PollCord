# PollCord Frontend

<p align="center"><img width=60.5% src="https://docs.pycord.dev/en/stable/_images/snake_dark.svg"></p>

The frontend for PollCord is a Python 3 app, or more specifically, a Discord bot made in Pycord. It is tested and covered by Pytest, Pytest-cov, and Testcord. The documentation is auto-generated using Sphinx, and which are automatically uploaded to a specified branch for GitHub Pages. We chose the frontend for its relatively short writing times and to take advantage of the new cutting-edge features of Pycord to create a sleek UI for making polls.

The bot itself is mostly self-sufficient, and only relies on a few database calls to run some validation and to save poll results for future recollection.

## Installation
Please refer to the INSTALL.md file within this directory for details on how to install.

## Testing
Once all the steps in INSTALL.md are done, then within the frontend folder, run the following:
```
pytest --cov=./
```

This should generate a report file upon a successful run of the test suite showing the passing tests and the coverage metrics.

## Structure
![PollCord frontend structure](https://user-images.githubusercontent.com/45674454/194627446-71c1c0b4-d16f-411f-bdf3-d7a0102c6741.png)

## Documentation
Please refer to the GitHub Pages for all the documentation for the frontend: [https://ntgomes.github.io/PollCord/](https://ntgomes.github.io/PollCord/).

## How to Use
`/makepoll {POLL NAME}`: Creates a poll with the given poll name, provided it does not exist in the database yet.
`/recallpoll {POLL NAME`: Retrieves a poll's full information, including results, to the user; assumes that the poll of the given poll name is already present in the database.

Other actions are self-explanatory from the sleek UI design. Please see the demo video for more details.
