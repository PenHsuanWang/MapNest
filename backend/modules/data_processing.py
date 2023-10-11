import geopandas as gpd

def load_shapefile(file_path):
    return gpd.read_file(file_path)

# 其他與地理資料處理相關的功能也可以在此模組中實現
