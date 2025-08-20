const fs = require('fs').promises;
const path = require('path');
const { v4: uuidv4 } = require('uuid');
const postcardsPath = path.resolve(__dirname, '..', 'postcards.json');

async function getPostCardAll() {

    try {
        let raw;

        try {
            raw = await fs.readFile(postcardsPath, 'utf8');
            if (!raw.trim()) raw = '[]';
        } catch (err) {
            if (err.code === 'ENOENT') {
                await fs.writeFile(postcardsPath, '[]', 'utf8');
                raw = '[]';
            } else {
                throw err;
            }
        }

        const data = JSON.parse(raw);
        return Array.isArray(data) ? data : [];
    } catch (err) {
        err.status = 500;
        err.publicMessage = 'Falha ao ler postcards.';
        throw err;
    }
}

async function getPostCardById(id) {
    const targetId = String(id);

    try {
        const postcards = await getPostCardAll();
        const postcard = postcards.find(p => String(p.id) === targetId);

        if (!postcard) {
            const err = new Error('Cartão postal não encontrado.');
            err.status = 404;
            err.publicMessage = 'Cartão postal não encontrado.';
            throw err;
        }

        return postcard;
    } catch (err) {
        // [explicação] preserva 404 se já vier setado; só ajusta se não tiver status
        if (!err.status) {
            err.status = 500;
            err.publicMessage = 'Erro ao buscar cartão postal.';
        }
        throw err;
    }
}

async function postAddPostCard(body) {
    const { name, cidade, pais, descricao, imageUrl } = body;

    if (!name || !cidade || !pais || !descricao || !imageUrl) {
        const err = new Error('All fields are required.');
        err.status = 400;
        err.publicMessage = 'All fields are required.';
        throw err;
    }

    let raw;
    try {
        raw = await fs.readFile(postcardsPath, 'utf8');
        if (!raw.trim()) raw = '[]';
    } catch (e) {
        if (e.code === 'ENOENT') {
            await fs.writeFile(postcardsPath, '[]', 'utf8');
            raw = '[]';
        } else {
            throw e;
        }
    }

    const postcards = JSON.parse(raw);
    const newPostcard = {
        id: uuidv4(),
        name, cidade, pais, descricao, imageUrl,
    };

    postcards.push(newPostcard);
    await fs.writeFile(postcardsPath, JSON.stringify(postcards, null, 2), 'utf8');

    return newPostcard;
}
module.exports = { getPostCardAll, getPostCardById, postAddPostCard };
