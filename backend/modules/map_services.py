import folium
from . import data_processing

def create_base_map(start_coords=(23.6978, 120.9605)):
    """Create a base map with no layers."""
    return folium.Map(location=start_coords, zoom_start=8, tiles=None)

def add_tile_layer(map_object, layer='openstreetmap'):
    """Add a specified tile layer to the provided map."""
    tile_layers = {
        'openstreetmap': {
            'url': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            'attr': '© OpenStreetMap contributors'
        },
        'mapbox': {
            'url': 'https://api.mapbox.com/styles/v1/mapbox/bright-v9/tiles/256/{z}/{x}/{y}?access_token=YOUR_MAPBOX_TOKEN',
            'attr': 'Mapbox attribution'
        }
    }
    if layer in tile_layers:
        folium.TileLayer(
            tiles=tile_layers[layer]['url'],
            attr=tile_layers[layer]['attr']
        ).add_to(map_object)

def add_shapefile_layer(map_object, shapefile_path):
    """Add a shapefile layer to the provided map."""
    gdf = data_processing.load_shapefile(shapefile_path)
    folium.GeoJson(gdf).add_to(map_object)

def generate_map_with_layer(layer='openstreetmap'):
    m = create_base_map()
    add_tile_layer(m, layer)
    return m._repr_html_()

def generate_map_with_shapefile(shapefile_path, layer='openstreetmap'):
    m = create_base_map()
    add_tile_layer(m, layer)
    add_shapefile_layer(m, shapefile_path)
    return m._repr_html_()
