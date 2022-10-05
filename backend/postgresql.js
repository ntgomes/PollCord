const pg =require("pg");
require('dotenv').config()


const { Pool } = pg;

 var test=()=>{
    // NOTE: PostgreSQL creates a superuser by default on localhost using the OS username.

    const pool = new Pool({
        user: process.env.POSTGRES_USER,
        database: process.env.POSTGRES_DATABASE_NAME,
        password: process.env.POSTGRES_PASSWORD,
        host: process.env.POSTGRES_HOST,
        port: process.env.POSTGRES_PORT,
    });

    // const pool = new Pool({
    //     user: "postgres",
    //     database: "postgres",
    //     password: "Test@1234",
    //     host: "127.0.0.1",
    //     port: 5432,
    // });

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