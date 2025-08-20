const { MongoClient, ObjectId } = require('mongodb');

const url = 'mongodb://localhost:27017';
const client = new MongoClient(url);
const dbName = 'postcardsDB';
const collectionName = 'postcards';

async function connectToDatabase() {
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection(collectionName);
    return {collection, client};
};

async function getPostCardAll() {
    const {collection, client} = await connectToDatabase();
    try {
        const postcards = await collection.find({}).toArray();
        return postcards.map(p => ({ ...p, id: p._id.toString() }));
    } catch (err) {
        err.status = 500;
        err.publicMessage = 'Falha ao ler postcards.';
        throw err;
    }
    finally {
        await client.close();
    }
}

async function getPostCardById(id) {
    const {collection, client} = await connectToDatabase();

    try {
        const postcard = await collection.findOne({ _id: new ObjectId(id) });

        if (!postcard) {
            const err = new Error('Cartão postal não encontrado.');
            err.status = 404;
            err.publicMessage = 'Cartão postal não encontrado.';
            throw err;
        }
        return { ...postcard, id: postcard._id.toString() };
    } catch (err) {
        if (!err.status) {
            err.status = 500;
            err.publicMessage = 'Erro ao buscar cartão postal.';
        }
        throw err;
    } finally {
        await client.close();
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

    const newPostcard = { name, cidade, pais, descricao, imageUrl };

    const {collection, client} = await connectToDatabase();
    try {
        const result = await collection.insertOne(newPostcard);
        newPostcard.id = result.insertedId.toString();

        return newPostcard;
    } catch (err) {
        console.error('Erro ao adicionar cartão postal:', err);
        err.status = 500;
        throw err;
    } finally {
        await client.close();
    }
}

async function deletePostCardById(id) {
    const targetId = String(id);
    const {collection, client} = await connectToDatabase();
    try {
        const result = await collection.deleteOne({ _id: new ObjectId(targetId) });

        if (result.deletedCount === 0) {
            const err = new Error('Cartão postal não encontrado.');
            err.status = 404;
            err.publicMessage = 'Cartão postal não encontrado.';
            throw err;
        }

        return { message: 'Cartão postal deletado com sucesso.' };
    } catch (err) {
        if (!err.status) {
            err.status = 500;
            err.publicMessage = 'Erro ao deletar cartão postal.';
        }
        throw err;
    } finally {
        await client.close();
    }
}

module.exports = { getPostCardAll, getPostCardById, postAddPostCard, deletePostCardById };
