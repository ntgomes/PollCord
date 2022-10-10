# PollCord Backend

<p align="center"><img width=60.5% src="https://user-images.githubusercontent.com/36363608/194680835-35c6838b-b57d-4322-aa08-a8b40a83b8bc.png"></p>

The backend for PollCord is written in Node.js. The package manager used is npm. It is tested by our own test set-up and covered by a coverage package'nyc'. Node.js was used for its performance and scalability. PostgreSql is used as the database tool

## Installation
Please refer to the INSTALL.md file within this directory for details on how to install.

## Testing
The postgres backend needs to be up and running in-order for the testing or coverage to work, due to this, adding it in github actions is not viable. So we perform testing and coverage via other methods.
other methods -> our own test set-up and a coverage package "nyc"
<p align="center"><img width=40.5% src="https://user-images.githubusercontent.com/36363608/194782311-3296bc01-0cc5-4948-9e27-8e1a1db56630.png"></p>


## Documentation
Due to technical difficulties we do not have the documentation for the backend yet. You can refer to the code comments for now until we have a proper documentation

## Structure
![PollCord backend structure](https://user-images.githubusercontent.com/36363608/194782264-84532096-0e38-4da9-b165-699a7d0e7577.png)

## Database ERD Diagram
![image](https://user-images.githubusercontent.com/36363608/194782581-afc19aec-f500-4db9-a2f7-ab00cfe8fd15.png)


## How to Use

- **Check if a poll exists:**

GET endpoint → “/check/{guild_id}/{poll_name}”

Returns: True if poll exists; false otherwise
```
{
    “exists”: true/false
}
```  


- **Save Poll Results:**

POST endpoint → “/save”

Accepts request body in a format similar to this:
```
{
    “guild_id”: 1294898934,
    “poll_name”: “my_poll”,
    “results”: {
        “question1”: {
            "question_text": "How is the project going?",
            “Option1_text”: 10,
            “Option2_text”: 26,
            “Option3_text”: 13
        },
	“question2”...
    }
}
```

Returns the following response: True if saved successfully; false otherwise
```
{
    "success": true/false
}
```


- **Recall Poll:**

GET endpoint → “/recall/{guild_id}/{poll_name}”

Returns the poll information if so, and None otherwise. Looks like the following:
```
{
    “guild_id”: 1294898934,
    “poll_name”: “my_poll”,
    “results”: {
        “question1”: {
            “Option1”: 10,
            “Option2”: 26,
            “Option3”: 13
        },
	“question2”...
    }
}
```
