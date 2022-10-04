import dotenv from "dotenv";
import express from "express";
import postgresql from "./postgresql.js";

dotenv.config();

// Create and Mock up, to clean up nicely and place in functions
postgresql(async (connection) => {
    // Create
    await connection.query(
        `
        CREATE TABLE IF NOT EXISTS polls (
            pollId SERIAL PRIMARY KEY,
            guildId varchar NOT NULL,
            pollName varchar NOT NULL
        );
        `
    );

    await connection.query(
        `
        CREATE TABLE IF NOT EXISTS questions (
            questionId SERIAL PRIMARY KEY,
            pollId int REFERENCES polls(pollId), 
            questionText varchar NOT NULL
        );
        `
    );

    await connection.query(
        `
        CREATE TABLE IF NOT EXISTS options (
            questionId int REFERENCES questions(questionId),
            optionText varchar,
            count int NOT NULL
        );
        `
    );

    console.log("PostgreSQL database Created");

    const json_input = {
        guild_id: 1294898934,
        poll_name: "my_poll",
        results: {
            question1: {
                question_text: "How is the project going?",
                Option1: 10,
                Option2: 26,
                Option3: 13,
            },
            question2: {
                question_text: "How is the semester?",
                Option1: 1,
                Option2: 6,
                Option3: 3,
                Option4: 2,
            },
        },
    };

    let guild_id = json_input["guild_id"];
    let poll_name = json_input["poll_name"];
    let results = json_input["results"];

    const response = await connection.query(
        `
        Insert into polls (guildId, pollName)
        values ('${guild_id}', '${poll_name}');
        `
    );

    const poll_id_getter = await connection.query(
        `
        Select pollId from polls where pollName='${poll_name}';
        `
    );
    console.log(poll_id_getter);
    const poll_id = poll_id_getter[0]["pollid"];
    console.log(poll_id);

    for (var question_num in results) {
        // var q_string = "question"+i.toString();
        var question = results[question_num];
        var question_text = question["question_text"];
        console.log(question_num);
        const question_inserter = await connection.query(
            `
            Insert into questions (pollId, questionText) 
            VALUES ('${poll_id}', '${question_text}');
            `
        );

        const question_id_getter = await connection.query(
            `
            Select questionId from questions where pollId='${poll_id}' and questionText='${question_text}';
            `
        );
        const question_id = question_id_getter[0]["questionid"];

        for (var field in results[question_num]) {
            if (field == "question_text") {
                continue;
            }
            var option_count = results[question_num][field];

            const option_inserter = await connection.query(
                `
                Insert into options (questionId, optionText, count) 
                VALUES ('${question_id}', '${field}', '${option_count}');
                `
            );
        }
    }

    // console.log("PostgreSQL database seeded!");
});

const app = express();

// app.get("/check", async (req, res) => {
//     // console.log(req.body);

//     // const { pollName } = req.body;
//     const rows = await process.postgresql.query(
//         `select exists(select 1 from poll where pollName=${pollName})`
//     );

//     res.status(200).json({ exists: rows });

//     // res.status(200).send(JSON.stringify(rows));
// });

// app.get("/recall", async (req, res) => {
//     const rows = await process.postgresql.query("SELECT * FROM poll");
//     res.status(200).send(JSON.stringify(rows));
// });

// app.get("/save", async (req, res) => {
//     console.log(req.body);
//     const rows = await process.postgresql.query("SELECT * FROM poll");
//     res.status(200).send(JSON.stringify(rows));
// });

app.listen(3000, () => {
    console.log("App running at http://localhost:3000");
});
