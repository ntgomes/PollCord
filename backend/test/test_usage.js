require("dotenv").config();
const postgresql = require("../postgresql");
var connection = postgresql();
const needle = require("needle");
var clc = require("cli-color");

console.log("Started testing ...");

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

var succesfull = 0;
console.log(clc.blue("\nTrying to Delete all existing DB content"));

// remove all data from all tables, assuming that tables exist
function test_setup() {
    (async () => {
        await connection
            .query(
                `
            TRUNCATE polls CASCADE;
            `
            )
            .then(() => {
                console.log(clc.green("Deleted"));
                console.log(clc.blue("\nTesting /save endpoint"));
                needle(
                    "post",
                    `http://localhost:${process.env.APP_PORT}/save`,
                    data,
                    {
                        json: true,
                    }
                )
                    .then((res) => {
                        console.log(clc.green(`Status: ${res.statusCode}`));
                        console.log(clc.blue("\nTesting /recall endpoint"));
                        succesfull += 1;

                        needle(
                            "get",
                            `http://localhost:${process.env.APP_PORT}/recall/1294898935/my_poll2`,
                            data,
                            {
                                json: true,
                            }
                        )
                            .then((res) => {
                                console.log(
                                    clc.green(`Status: ${res.statusCode}`)
                                );
                                console.log(
                                    clc.blue("\nTesting /check endpoint")
                                );
                                succesfull += 1;

                                needle(
                                    "get",
                                    `http://localhost:${process.env.APP_PORT}/check/1294898935/my_poll2`,
                                    data,
                                    {
                                        json: true,
                                    }
                                )
                                    .then((res) => {
                                        succesfull += 1;
                                        console.log(
                                            clc.green(
                                                `Status: ${res.statusCode}`
                                            )
                                        );
                                        console.log(
                                            clc.green(
                                                `\nSuccesfully ran: ${succesfull} out of 3 test cases.`
                                            )
                                        );
                                        return 1;
                                    })
                                    .catch((err) => {
                                        console.error(err);
                                        console.log(
                                            clc.green(
                                                `\nSuccesfully ran: ${succesfull} out of 3 test cases.`
                                            )
                                        );
                                        console.log(
                                            clc.red(
                                                `\nFailed in: ${
                                                    3 - succesfull
                                                } out of 3 test cases.`
                                            )
                                        );
                                        return 0;
                                    });
                            })
                            .catch((err) => {
                                console.error(err);
                                console.log(
                                    clc.green(
                                        `\nSuccesfully ran: ${succesfull} out of 3 test cases.`
                                    )
                                );
                                console.log(
                                    clc.red(
                                        `\nFailed in: ${
                                            3 - succesfull
                                        } out of 3 test cases.`
                                    )
                                );
                                return 0;
                            });
                    })
                    .catch((err) => {
                        console.error(err);
                        console.log(
                            clc.green(
                                `\nSuccesfully ran: ${succesfull} out of 3 test cases.`
                            )
                        );
                        console.log(
                            clc.red(
                                `\nFailed in: ${
                                    3 - succesfull
                                } out of 3 test cases.`
                            )
                        );
                        return 0;
                    });
            });
    })().catch((err) => {
        console.error(err);
        console.log(
            clc.green(`\nSuccesfully ran: ${succesfull} out of 3 test cases.`)
        );
        console.log(
            clc.red(`\nFailed in : ${3 - succesfull} out of 3 test cases.`)
        );
        return 0;
    });
}

if (typeof require !== "undefined" && require.main === module) {
    test_setup();
}

module.exports = { test_setup };
