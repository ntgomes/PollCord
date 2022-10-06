require("dotenv").config();

const postgresql = require("../postgresql");

var connection = postgresql();
connection
    .query(
        `
    CREATE TABLE IF NOT EXISTS polls (
        pollId SERIAL PRIMARY KEY,
        guildId varchar NOT NULL,
        pollName varchar NOT NULL
    );
    `
    )
    .then(() => {
        connection
            .query(
                `
        CREATE TABLE IF NOT EXISTS questions (
            questionId SERIAL PRIMARY KEY,
            pollId int REFERENCES polls(pollId), 
            questionText varchar NOT NULL
        );
        `
            )
            .then(() => {
                connection
                    .query(
                        `
            CREATE TABLE IF NOT EXISTS options (
                questionId int REFERENCES questions(questionId),
                optionText varchar,
                count int NOT NULL
            );
            `
                    )
                    .then(() => {
                        console.log("DB creation successfull");
                    });
            });
    });
