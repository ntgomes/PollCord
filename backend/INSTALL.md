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
npm clean install
```

4. Change the .env file according to the Postgres installation and run the following commands
``` 
npm run setup
```

5. Run the server Script
```
node server.js
```
