const express = require('express');
const router = express.Router();
const { Post } = require('../models');

// Afficher le formulaire
router.get('/post', (req, res) => {
  res.render('post-form');
});

// Gérer la soumission du formulaire
router.post('/post', async (req, res) => {
  const { content, difficulte, resonnance } = req.body;
  await Post.create({ content, difficulte, resonnance });
  res.redirect('/post/success'); // ou autre page de confirmation
});

module.exports = router;
