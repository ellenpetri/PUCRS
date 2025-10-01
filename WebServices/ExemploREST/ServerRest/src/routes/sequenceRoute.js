const sequenceController = require('../controllers/sequenceController.js');

module.exports = (app) => {
    app.post('/sequence', sequenceController.post);
    app.put('/sequence', sequenceController.put);
    app.delete('/sequence', sequenceController.delete);
    app.get('/sequences', sequenceController.get);
    app.get('/sequence/:id', sequenceController.getById);
}