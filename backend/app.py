from flask import Flask, jsonify, request
from modules import map_services
import folium

app = Flask(__name__)


@app.route('/generate_map')
def generate_map():
    layer = request.args.get('layer', 'openstreetmap')  # 取得使用者選擇的圖層。

    map_html = map_services.generate_map_with_layer(layer)  # 使用 generate_map_with_layer 生成地圖。

    start_coords = (23.6978, 120.9605)
    zoom_level = 8

    return jsonify({"map_html": map_html, "start_coords": start_coords, "zoom_level": zoom_level})


@app.route('/generate_map_with_shapefile', methods=['POST'])
def generate_map_with_shapefile():
    layer = request.form.get('layer', 'openstreetmap')
    shapefile_path = request.form['shapefile_path']

    map_html = map_services.generate_map_with_shapefile(shapefile_path, layer)
    return jsonify({"map_html": map_html})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
