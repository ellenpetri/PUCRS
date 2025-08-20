var express = require('express');
var router = express.Router();
const { getPostCardAll } = require('../controllers/postcards');

router.get('/', async (req, res) => {
  try {
    const postcards = await getPostCardAll();
    res.render('home', { postcards });
  } catch (err) {
    console.error(err);
    res
      .status(err.status || 500)
      .render('error', { message: err.publicMessage || 'Erro interno.', error: err });
  }
});

module.exports = router;
