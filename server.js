const express = require('express');
const dotenv = require('dotenv');
const errorHandle = require('./middleware/error');
const connectDb = require('./config/db');
const cors = require
dotenv.config({path: './config/config.env'});
const app = express();
const PORT = process.env.PORT;

connectDb();

app.use(express.json());
const keyword = require('./routes/keyword');

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.use(errorHandle);
app.use('/api/v1/keyword',keyword);
const server = app.listen(PORT, () => {
    console.log('App listening on port ',PORT);
});

process.on('unhandledRejection',(err,promise) =>{
    console.log(err);
    server.close(()=>process.exit(1));
})