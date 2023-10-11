from flask import Flask, jsonify, request
from modules import map_services

app = Flask(__name__)


@app.route('/generate_map/<layer>', methods=['GET'])
def generate_map(layer='openstreetmap'):
    map_html = map_services.generate_map_with_layer(layer)
    return jsonify({"map_html": map_html})


@app.route('/generate_map_with_shapefile', methods=['POST'])
def generate_map_with_shapefile():
    layer = request.form.get('layer', 'openstreetmap')
    shapefile_path = request.form['shapefile_path']

    map_html = map_services.generate_map_with_shapefile(shapefile_path, layer)
    return jsonify({"map_html": map_html})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
