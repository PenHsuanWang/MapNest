const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', './src/views');

app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5001/generate_map/openstreetmap');
        const mapHtml = response.data.map_html;
        res.render('index', { map: mapHtml });
    } catch (error) {
        console.error("Error fetching map:", error);
        res.status(500).send("Error fetching map.");
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
