# PollCord Backend

<p align="center"><img width=60.5% src="https://user-images.githubusercontent.com/36363608/194680835-35c6838b-b57d-4322-aa08-a8b40a83b8bc.png"></p>

The backend for PollCord is written in Node.js. The package manager used is npm. It is tested and covered by {}. Node.js was used for its performance and scalability. The documentation is auto-generated using Sphinx, and which are automatically uploaded to a specified branch for GitHub Pages. PostgreSql is used as the database tool

## Installation
Please refer to the INSTALL.md file within this directory for details on how to install.

## Testing
Once all the steps in INSTALL.md are done, then within the backend folder, run the following:

{pytest --cov=./}
This should generate a report file upon a successful run of the test suite showing the passing tests and the coverage metrics.

## Structure
![PollCord backend structure](https://user-images.githubusercontent.com/36363608/194679509-5913f2b6-d8a9-4d8e-8157-101a241cef0f.png)

## Documentation
Please refer to the GitHub Pages for all the documentation for the frontend: [https://ntgomes.github.io/PollCord/](https://ntgomes.github.io/PollCord/).

## How to Use
`GET endpoint → /check/{guild_id}/{poll_name}`: Returns true if the poll with the given poll name

`POST endpoint → /save`: Saves the poll with the given poll name

`GET endpoint → /recall/{guild_id}/{poll_name}`: Returns the poll with the given poll name
