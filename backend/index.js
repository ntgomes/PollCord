import dotenv from "dotenv";
import express from "express";
import postgresql from "./postgresql.js";

dotenv.config();

postgresql(async (connection) => {
    await connection.query(
        `
        CREATE TABLE IF NOT EXISTS poll (
            id SERIAL PRIMARY KEY,
            guildId bigint NOT NULL,
            pollName varchar NOT NULL,
            question varchar,
            option varchar
        );
        `
    );
    // await connection.query(
    //     "CREATE UNIQUE INDEX IF NOT EXISTS guildId ON poll (guildId);"
    // );
    console.log("PostgreSQL database Created");

    const options = [
        {
            guildId: 2,
            pollName: "test2",
            question: "Where am I?",
            option: "A",
        },
        {
            guildId: 2,
            pollName: "test2",
            question: "Where am I?",
            option: "B",
        },
        {
            guildId: 2,
            pollName: "test2",
            question: "Where am I?",
            option: "C",
        },
        {
            guildId: 2,
            pollName: "test2",
            question: "Where am I?",
            option: "D",
        },
    ];

    for (let i = 0; i < options.length; i += 1) {
        const option = options[i];
        await connection.query(
            `INSERT INTO poll (guildId, pollName, question, option) 
            VALUES ('${option.guildId}', '${option.pollName}','${option.question}','${option.option}') 
            ON CONFLICT DO NOTHING;`
        );
    }

    console.log("PostgreSQL database seeded!");
});

const app = express();

app.get("/check", async (req, res) => {
    const rows = await process.postgresql.query("");
    res.status(200).send(JSON.stringify(rows));
});

app.get("/polls", async (req, res) => {
    const rows = await process.postgresql.query("SELECT * FROM poll");
    res.status(200).send(JSON.stringify(rows));
});

app.listen(3000, () => {
    console.log("App running at http://localhost:3000");
});
