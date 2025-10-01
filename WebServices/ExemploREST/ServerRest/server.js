const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3010;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

app.get('/', (req, res) => {
    res.send('Hello World!');
});

require('./src/Routes/index')(app);