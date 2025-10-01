const SequenceRoute = require('./sequenceRoute');

module.exports = (app) => {
    app.use('/sequences', SequenceRoute);
};