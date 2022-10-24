const mongoose = require('mongoose')
const videoSchema = mongoose.Schema({
    videoId: {
        type: String,
        required: ['true','Video ID is mandatory'],
        unique: true
    },
    query: [
        {
            key: String,
            count: Number
        }
    ]
})

module.exports = mongoose.model('Video',videoSchema);