from flask import Flask, jsonify, request
from modules import map_services
import folium

app = Flask(__name__)


@app.route('/generate_map')
def generate_map():
    start_coords = (23.6978, 120.9605)
    zoom_level = 8
    map_object = folium.Map(location=start_coords, zoom_start=zoom_level)
    map_html = map_object._repr_html_()
    return jsonify({"map_html": map_html, "start_coords": start_coords, "zoom_level": zoom_level})



@app.route('/generate_map_with_shapefile', methods=['POST'])
def generate_map_with_shapefile():
    layer = request.form.get('layer', 'openstreetmap')
    shapefile_path = request.form['shapefile_path']

    map_html = map_services.generate_map_with_shapefile(shapefile_path, layer)
    return jsonify({"map_html": map_html})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
