const express = require("express");
require("dotenv").config();

const postgresql = require("./postgresql");

const app = express();

let bodyParser = require("body-parser");

const port = process.env.APP_PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/check/:guild_id/:poll_name", async (req, res) => {
    

    const poll_name = req.params.poll_name.replace(/'/g, "''");
    if(!poll_name||!req.params.guild_id){
        res.status(500).json({"text": "Please provide all the required params"});
        return;
    }

    const rows = await postgresql().query(
        `
        select exists(select 1 from polls 
        where guildId='${req.params.guild_id}' and pollName='${poll_name}');
        `
    );
    res.status(200).json(rows[0]);
});

app.post("/save", async (req, res) => {
    var connection = postgresql();

    var json_input = req.body;
    let guild_id = json_input["guild_id"];
    let poll_name = json_input["poll_name"];
    let results = json_input["results"];

    // if these fields are empty, then return a failure
    if (!guild_id  ||
        !poll_name  ||
        !results) {
        res.status(200).json({ success: false });
        return;
    }

    // if there is an apostrophe, replace it with double-single-quote
    poll_name = poll_name.replace(/'/g, "''");

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

    const poll_id = poll_id_getter[0]["pollid"];

    for (var question_num in results) {
        var question = results[question_num];
        var question_text = question["question_text"];

        question_text = question_text.replace(/'/g, "''");

        const question_inserter = await connection.query(
            `
            Insert into questions (pollId, questionText) 
            VALUES ('${poll_id}', '${question_text}');
            `
        );

        const question_id_getter = await connection.query(
            `
            Select questionId from questions 
            where pollId='${poll_id}' and questionText='${question_text}';
            `
        );
        const question_id = question_id_getter[0]["questionid"];

        for (var field in results[question_num]) {
            if (field == "question_text") {
                continue;
            }
            var option_count = results[question_num][field];

            field = field.replace(/'/g, "''");
            const option_inserter = await connection.query(
                `
                Insert into options (questionId, optionText, count) 
                VALUES ('${question_id}', '${field}', '${option_count}');
                `
            );
        }
    }

    res.status(200).json({ success: true });
});

app.get("/recall/:guild_id/:poll_name", async (req, res) => {
    var results = {};
    var poll_name = req.params.poll_name.replace(/'/g, "''");

    const rows = await postgresql().query(
        `
        SELECT * FROM polls 
        where pollname='${poll_name}' and guildid='${req.params.guild_id}';
        `
    );

    for (var i = 0; i < rows.length; i++) {
        var id = rows[i].pollid;
        const rows1 = await postgresql().query(
            `
            SELECT * FROM questions 
            where pollid=${id};
            `
        );

        for (var j = 0; j < rows1.length; j++) {
            var x = {};
            x["question_text"] = rows1[j].questiontext;

            const rows2 = await postgresql().query(
                `
                SELECT * FROM options 
                where questionid='${rows1[j].questionid}';
                `
            );

            for (var k = 0; k < rows2.length; k++) {
                x[rows2[k].optiontext] = rows2[k].count;
            }

            var temp = j + 1;
            results["question" + temp] = x;
        }
    }
    const json_output = {
        guild_id: req.params.guild_id,
        poll_name: req.params.poll_name,
        results: results,
    };
    res.status(200).send(json_output);
});

app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});
