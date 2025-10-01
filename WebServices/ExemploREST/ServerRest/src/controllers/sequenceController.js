exports.post = (req, res, next) => {
    res.status(201).send('Route POST');
};
exports.put = (req, res, next) => {
    console.log(req.body);
    let id = req.body.id;
    if (!id) {
        return res.status(400).send('ID is required');
    }
    res.status(200).send('Route PUT with id: ' + id );
}
exports.delete = (req, res, next) => {
    let id = req.body.id;
    if (!id) {
        return res.status(400).send('ID is required');
    }
    res.status(200).send('Route DELETE with id: ' + id);
};
exports.get = (req, res, next) => {
    res.status(200).send('Route GET all');
}
exports.getById = (req, res, next) => {
    let id = req.params.id;
    if (!id) {
        return res.status(400).send('ID is required');
    }
    res.status(200).send('Route GET with id: ' + id);
};