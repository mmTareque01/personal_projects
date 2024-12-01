const mongoose = require('mongoose');
const MONGO_URI = process.env.MONGO_URI || "mongodb+srv://mmtareque:pzuwDw3l7NrE3nB0@cluster0.tj0sdq8.mongodb.net/HMS";

const connectDatabase = () => {
    mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
        .then(() => {
            console.log("Mongoose Connected");
        });
}

module.exports = connectDatabase;