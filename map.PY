{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8d7cd936",
   "metadata": {},
   "outputs": [],
   "source": [
    "import geopandas as gpd\n",
    "from matplotlib import pyplot as plt\n",
    "import mapclassify as mc\n",
    "import folium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c657aeaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# --- FUNCTION TO LOAD AND FIX CRS ---\n",
    "def load_shp(path):\n",
    "    data = gpd.read_file(path)\n",
    "    if data.crs is None:\n",
    "        # Assuming Lat/Long if missing. Change to 32644 if it's a local AP map\n",
    "        data.set_crs(epsg='4326', inplace=True)\n",
    "    else:\n",
    "        data = data.to_crs(epsg='4326')\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e5697636",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# 1. Load both Shapefiles\n",
    "# Replace these with your actual filenames\n",
    "shp1 = load_shp(r'D:\\\\harsh\\\\map\\\\91\\\\MAJOR_TOWNS.shp') \n",
    "shp2 = load_shp(r'D:\\\\harsh\\\\map\\\\91\\\\DISTRICT_HQ.shp')\n",
    "shp3 = load_shp(r'D:\\\\harsh\\\\map\\\\91\\\\DISTRICT_BOUNDARY.shp') \n",
    "shp4 = load_shp(r'D:\\\\harsh\\\\map\\\\91\\\\STATE_BOUNDARY.shp')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a4d75298",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# 2. Initialize the map centered on India\n",
    "m = folium.Map(location=[22.0, 78.0], zoom_start=5, tiles=\"Cartodb Positron\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e953cb26",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# 3. Create Layer\n",
    "#  1 (e.g., India State Boundaries)\n",
    "layer1 = folium.FeatureGroup(name=\"major towns\")\n",
    "for idx, row in shp1.iterrows():\n",
    "\n",
    "    if row.geometry is None:\n",
    "        continue\n",
    "\n",
    "    folium.CircleMarker(\n",
    "        location=[row.geometry.y, row.geometry.x],\n",
    "        radius=2,\n",
    "        color='blue',\n",
    "        fill=True,\n",
    "        fill_color='blue',\n",
    "        fill_opacity=0.8,\n",
    "        popup=str(row[shp1.columns[0]])\n",
    "    ).add_to(layer1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "543de60f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# 4. Create Layer 2 (e.g., Amaravati or Players)\n",
    "layer2 = folium.FeatureGroup(name=\"District HQ\")\n",
    "for idx, row in shp2.iterrows():\n",
    "\n",
    "    if row.geometry is None:\n",
    "        continue\n",
    "\n",
    "    folium.CircleMarker(\n",
    "        location=[row.geometry.y, row.geometry.x],\n",
    "        radius=3,\n",
    "        color='red',\n",
    "        fill=True,\n",
    "        fill_color='red',\n",
    "        fill_opacity=0.8,\n",
    "        popup=str(row[shp2.columns[0]])\n",
    "    ).add_to(layer2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "67448bc7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<folium.features.GeoJson at 0x20c4fc2f750>"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# ---------------- LAYER 3 ----------------\n",
    "layer3 = folium.FeatureGroup(name=\"District Boundary\")\n",
    "\n",
    "folium.GeoJson(\n",
    "    shp3,\n",
    "    style_function=lambda x: {\n",
    "        'fillColor': 'none',\n",
    "        'color': 'green',\n",
    "        'weight': 1\n",
    "    },\n",
    "    tooltip=folium.GeoJsonTooltip(fields=[shp3.columns[0]])\n",
    ").add_to(layer3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "89925926",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<folium.features.GeoJson at 0x20d45574550>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# ---------------- LAYER 4 ----------------\n",
    "layer4 = folium.FeatureGroup(name=\"State Boundary\")\n",
    "\n",
    "folium.GeoJson(\n",
    "    shp4,\n",
    "    style_function=lambda x: {\n",
    "        'fillColor': 'none',\n",
    "        'color': 'black',\n",
    "        'weight': 2\n",
    "    },\n",
    "    tooltip=folium.GeoJsonTooltip(fields=[shp4.columns[0]])\n",
    ").add_to(layer4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "a67d1678",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<folium.map.FeatureGroup at 0x20cd63333e0>"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# 5. Add both layers to the map\n",
    "layer1.add_to(m)\n",
    "layer2.add_to(m)\n",
    "layer3.add_to(m)\n",
    "layer4.add_to(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c2f53160",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<folium.map.LayerControl at 0x20b4c7febe0>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# 6. Add Layer Control (The toggle box)\n",
    "folium.LayerControl().add_to(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "ae3a8b00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Map with 2 layers saved as 'dual_layer_map.html'\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# 7. Save\n",
    "m.save(\"dual_layer_map.html\")\n",
    "print(\"Map with 2 layers saved as 'dual_layer_map.html'\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
