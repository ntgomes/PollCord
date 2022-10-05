require('dotenv').config()

const postgresql= require(  "../postgresql");



// Create and Mock up, to clean up nicely and place in functions
var connection = postgresql();
 // Create
  connection.query(
    `
    CREATE TABLE IF NOT EXISTS polls (
        pollId SERIAL PRIMARY KEY,
        guildId varchar NOT NULL,
        pollName varchar NOT NULL
    );
    `
).then((res)=>{
    connection.query(
        `
        CREATE TABLE IF NOT EXISTS questions (
            questionId SERIAL PRIMARY KEY,
            pollId int REFERENCES polls(pollId), 
            questionText varchar NOT NULL
        );
        `
    ).then(res1=>{
        connection.query(
            `
            CREATE TABLE IF NOT EXISTS options (
                questionId int REFERENCES questions(questionId),
                optionText varchar,
                count int NOT NULL
            );
            `
        ).then(res2=>{
            console.log("DB creation scucesfull");
        });
    });
    
});

 





