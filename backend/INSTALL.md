# Installation

Following are the guidelines to install the PollCord backend software on any device in a few easy steps:

**Prerequisites**: 
The following tools need to be already installed on your device
  - Node.js
  - Postgres db


## Guidelines:
1. Clone the PollCord Repository at a suitable location on your local device **(Skip if already cloned)**

```
git clone https://github.com/ntgomes/PollCord.git 
```
2. Checkout to the Pollcord directory. Then checkout to the backend directory
```
cd PollCord 
cd backend
```

3. Start a terminal/ Command prompt session and run npm
```
npm install
```

4. Create a user in the postgresql db using the following command
```
CREATE USER postgres
 ```
 
5. Create a default Postgres Database and grant all permissions to the above user
```
CREATE DATABASE postgres
GRANT ALL
    ON postgres
    TO postgres
    
``` 
6. Change the values in the .env file according to the Postgres installation and run the following commands
``` 
npm run setup
```

7. Run the server Script
```
node run start
```
