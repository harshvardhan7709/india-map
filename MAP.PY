import geopandas as gpd
from matplotlib import pyplot as plt
import mapclassify as mc
import folium

# --- FUNCTION TO LOAD AND FIX CRS ---
def load_shp(path):
    data = gpd.read_file(path)
    if data.crs is None:
        # Assuming Lat/Long if missing. Change to 32644 if it's a local AP map
        data.set_crs(epsg='4326', inplace=True)
    else:
        data = data.to_crs(epsg='4326')
    return data

# 1. Load both Shapefiles
# Replace these with your actual filenames
shp1 = load_shp(r'D:\\harsh\\map\\91\\MAJOR_TOWNS.shp') 
shp2 = load_shp(r'D:\\harsh\\map\\91\\DISTRICT_HQ.shp')
shp3 = load_shp(r'D:\\harsh\\map\\91\\DISTRICT_BOUNDARY.shp') 
shp4 = load_shp(r'D:\\harsh\\map\\91\\STATE_BOUNDARY.shp')

# 2. Initialize the map centered on India
m = folium.Map(location=[22.0, 78.0], zoom_start=5, tiles="Cartodb Positron")

# 3. Create Layer
#  1 (e.g., India State Boundaries)
layer1 = folium.FeatureGroup(name="major towns")
for idx, row in shp1.iterrows():

    if row.geometry is None:
        continue

    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=2,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.8,
        popup=str(row[shp1.columns[0]])
    ).add_to(layer1)
    
# 4. Create Layer 2 (e.g., Amaravati or Players)
layer2 = folium.FeatureGroup(name="District HQ")
for idx, row in shp2.iterrows():

    if row.geometry is None:
        continue

    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=3,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.8,
        popup=str(row[shp2.columns[0]])
    ).add_to(layer2)
    
# ---------------- LAYER 3 ----------------
layer3 = folium.FeatureGroup(name="District Boundary")

folium.GeoJson(
    shp3,
    style_function=lambda x: {
        'fillColor': 'none',
        'color': 'green',
        'weight': 1
    },
    tooltip=folium.GeoJsonTooltip(fields=[shp3.columns[0]])
).add_to(layer3)

# ---------------- LAYER 4 ----------------
layer4 = folium.FeatureGroup(name="State Boundary")

folium.GeoJson(
    shp4,
    style_function=lambda x: {
        'fillColor': 'none',
        'color': 'black',
        'weight': 2
    },
    tooltip=folium.GeoJsonTooltip(fields=[shp4.columns[0]])
).add_to(layer4)

# 5. Add both layers to the map
layer1.add_to(m)
layer2.add_to(m)
layer3.add_to(m)
layer4.add_to(m)

# 6. Add Layer Control (The toggle box)
folium.LayerControl().add_to(m)

# 7. Save
m.save("layer_map.html")
print("Map with 4 layers saved as 'layer_map.html'")
