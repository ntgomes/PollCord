require("dotenv").config();
const postgresql = require("../postgresql");
var connection = postgresql();
const needle = require("needle");

// console.log(process.env);
// console.log(process.env.POSTGRES_DATABASE_NAME);

const data = {
    guild_id: 1294898935,
    poll_name: "my_poll2",
    results: {
        question1: {
            question_text: "How is the project going?",
            Option1_text: 10,
            Option2_text: 26,
            Option3_text: 13,
        },
        question2: {
            question_text: "Will the project be done?",
            Option1_text: 1,
            Option2_text: 6,
            Option3_text: 3,
            Option4_text: 4,
        },
    },
};

// remove all data from all tables, assuming that tables exist
(async () => {
    // console.log(connection);
    await connection
        .query(
            `
        TRUNCATE polls CASCADE;
        `
        )
        .then(() => {
            console.log("Deleted all content");

            needle(
                "post",
                `http://localhost:${process.env.APP_PORT}/save`,
                data,
                {
                    json: true,
                }
            )
                .then((res) => {
                    console.log(`Status: ${res.statusCode}`);
                    console.log("Body: ", res.body);
                    needle(
                        "get",
                        `http://localhost:${process.env.APP_PORT}/recall/1294898935/my_poll2`,
                        data,
                        {
                            json: true,
                        }
                    )
                        .then((res) => {
                            console.log(`Status: ${res.statusCode}`);
                            console.log("Body: ", res.body);
                            needle(
                                "get",
                                `http://localhost:${process.env.APP_PORT}/check/1294898935/my_poll2`,
                                data,
                                {
                                    json: true,
                                }
                            )
                                .then((res) => {
                                    console.log(`Status: ${res.statusCode}`);
                                    console.log("Body: ", res.body);
                                })
                                .catch((err) => {
                                    console.error(err);
                                });
                        })
                        .catch((err) => {
                            console.error(err);
                        });
                })
                .catch((err) => {
                    console.error(err);
                });
        });
})().catch((err) => {
    console.error(err);
});
