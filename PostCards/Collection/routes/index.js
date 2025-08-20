var express = require('express');
var router = express.Router();
const { getPostCardAll } = require('../controllers/postcards');

router.get('/', async (req, res) => {
  try {
    const postcards = await getPostCardAll();
    res.json(postcards);
  } catch (err) {
    console.error(err);
    res
      .status(err.status || 500)
      .json({ error: err.publicMessage || 'Erro interno.' });
  }
});

module.exports = router;
