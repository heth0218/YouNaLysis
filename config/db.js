const mongoose = require('mongoose');

const connectDb = async () => {
    
    const conn = await mongoose.connect(process.env.URI_MONGODB,{
        useNewUrlParser:true,
        useUnifiedTopology: true,
    });
    console.log(`MongoDB connected: ${conn.connection.host}`);
}

module.exports = connectDb;