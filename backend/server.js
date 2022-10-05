const express = require('express')


const postgresql= require(  "./postgresql");


const app = express();

let bodyParser = require('body-parser');
const port = 3000

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));




app.post("/check/", async (req, res) => {
   


    const rows = await postgresql().query(
        `select exists(select 1 from polls where pollName='${req.body.poll_name}')`
    );

    res.status(200).json({ exists: rows });

    // res.status(200).send(JSON.stringify(rows));
});

app.post("/save", async (req, res) => {
 
    var connection = postgresql();
    var json_input = req.body;
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

const poll_id = poll_id_getter[0]["pollid"];


for (var question_num in results) {
    
    var question = results[question_num];
    var question_text = question["question_text"];
   
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

          res.status(200).json({"status":"Sucessfully saved"});
 
});
app.post("/recall", async (req, res) => {
    var results ={};
    const rows = await postgresql().query(`SELECT * FROM polls where pollname='${req.body.poll_name}' and guildid='${req.body.guild_id}'`);
    for(var i=0;i<rows.length;i++){
    var id = rows[i].pollid;
    const rows1 = await postgresql().query(`SELECT * FROM questions where pollid=${id}`);
   
 for(var j=0;j<rows1.length;j++){
var x={};
x["question_text"] = rows1[j].questiontext;
const rows2 = await postgresql().query(`SELECT * FROM options where questionid=${rows1[j].questionid}`);
for(var k=0;k<rows2.length;k++){
x[rows2[k].optiontext]=rows2[k].count;
}
results["question"+j]=x;

}
    }
    const json_input = {
        guild_id: req.query.guild_id,
        poll_name: req.query.poll_name,
        results: results,
    };
    res.status(200).send(json_input);
});
app.get("/",(req,res)=>{
    res.status(200).json({
        "ga":1
    });
})
app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })
