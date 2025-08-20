const express = require('express');
const router = express.Router();
const { getPostCardAll, getPostCardById, postAddPostCard, deletePostCardById } = require('../controllers/postcards');


// [GET] Todos os postcards
router.get('/', async (req, res) => {
  try {
    const postcards = await getPostCardAll();
    res.json(postcards);
  } catch (err) {
    console.error(err);
    res.status(err.status || 500).json({ error: err.publicMessage || 'Erro interno.' });
  }
});

// [GET] Postcard por ID
router.get('/:id', async (req, res) => {
  const postId = req.params.id;
  try {
    const postcard = await getPostCardById(postId); // <- passa o id aqui
    if (!postcard) {
      return res.status(404).json({ error: 'Cartão postal não encontrado.' });
    }
    res.json(postcard);
  } catch (err) {
    console.error(err);
    res.status(err.status || 500).json({ error: err.publicMessage || 'Erro interno.' });
  }
});

router.post('/', async (req, res) => {
  console.log('[POST /postcards] body =', req.body);
  try {
    const newPostcard = await postAddPostCard(req.body);
    res.status(201).json({ message: 'Cartão postal adicionado com sucesso.', newPostcard });
  } catch (err) {
    console.error('[POST /postcards] stack:', err.stack);
    res.status(err.status || 500).json({ error: err.publicMessage || 'Erro ao adicionar cartão postal.' });
  }
});

router.delete('/:id', async (req, res) => {
  const postId = req.params.id;
  try {
    await deletePostCardById(postId);
    res.status(204).send();
  } catch (err) {
    console.error(err);
    res.status(err.status || 500).json({ error: err.publicMessage || 'Erro ao deletar cartão postal.' });
  }
});

module.exports = router;
