const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.set('view engine', 'ejs');
app.set('views', './src/views');
app.use(express.static('public'));

app.get('/', async (req, res) => {
    const layer = req.query.layer || 'openstreetmap'; // 從查詢參數中取得圖層資訊
    try {
        const response = await axios.get(`http://localhost:5001/generate_map?layer=${layer}`);
        const mapHtml = response.data.map_html;
        const startCoords = response.data.start_coords;
        const zoomLevel = response.data.zoom_level;
        res.render('index', { map: mapHtml, startCoords: JSON.stringify(startCoords), zoomLevel: zoomLevel });
    } catch (error) {
        console.error("Error fetching map:", error);
        res.status(500).send("Error fetching map.");
    }
});



app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
