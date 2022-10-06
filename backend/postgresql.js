const pg = require("pg");
require("dotenv").config();

const { Pool } = pg;

var test = () => {
    // NOTE: Ensure to have a .env file containg these.
    const pool = new Pool({
        user: process.env.POSTGRES_USER,
        database: process.env.POSTGRES_DATABASE_NAME,
        password: process.env.POSTGRES_PASSWORD,
        host: process.env.POSTGRES_HOST,
        port: process.env.POSTGRES_PORT,
    });

    const connection = {
        pool,
        query: (...args) => {
            return pool.connect().then((client) => {
                return client.query(...args).then((res) => {
                    client.release();
                    return res.rows;
                });
            });
        },
    };

    return connection;
};

module.exports = test;
