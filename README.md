# 🗺️ India Interactive Map — GIS Visualization with Folium

A Python-based GIS project that generates an **interactive, multi-layer map of India** using shapefiles and Folium. The output is a fully browsable HTML map with toggleable layers for state boundaries, district boundaries, district headquarters, and major towns.

---

## 📌 Overview

This project reads official Indian geographic shapefiles and renders them as an interactive web map centered on India. Each geographic feature (towns, HQs, boundaries) is displayed on a separate toggleable layer, making it easy to explore and analyze spatial data.

**Output:** `layer_map.html` — an interactive map you can open directly in any browser.

---

## 📁 Repository Structure

```
india-map/
│
├── MAP.PY          # Standalone Python script version
├── map.PY          # Jupyter Notebook version (.ipynb exported as .PY)
└── README.md       # Project documentation
```

> **Note:** The project requires local shapefiles (not included in the repo). See the [Setup](#-setup--usage) section for details.

---

## 🗂️ Map Layers

The map renders **4 independent, toggleable layers**:

| Layer | Color | Type | Description |
|-------|-------|------|-------------|
| Major Towns | 🔵 Blue | Point (CircleMarker) | Major urban centres across India |
| District HQ | 🔴 Red | Point (CircleMarker) | District headquarter locations |
| District Boundary | 🟢 Green | Polygon (GeoJson) | Internal district-level boundaries |
| State Boundary | ⚫ Black | Polygon (GeoJson) | Outer state-level boundaries |

All layers have **interactive popups/tooltips** showing feature names on click or hover.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `geopandas` | Reading and reprojecting `.shp` shapefiles |
| `folium` | Generating the interactive Leaflet.js HTML map |
| `mapclassify` | Map classification (for potential choropleth use) |
| `matplotlib` | Static plot support |

---

## 📦 Required Shapefiles

Place the following `.shp` files in a local directory and update the paths in the script:

```
MAJOR_TOWNS.shp
DISTRICT_HQ.shp
DISTRICT_BOUNDARY.shp
STATE_BOUNDARY.shp
```

> These are standard Survey of India / Census of India GIS datasets. They are **not** bundled in this repo due to size/licensing.

---

## 🚀 Setup & Usage



### 1. Clone the Repository

```bash
git clone https://github.com/harshvardhan7709/india-map.git
cd india-map
```

### 2. Install Dependencies

```bash
pip install geopandas folium mapclassify matplotlib
```

> On Windows, installing via conda is recommended for smoother dependency handling:
> ```bash
> conda install geopandas folium
> ```

### 3. Update Shapefile Paths

In `MAP.PY`, update the file paths to point to your local shapefiles:

```python
shp1 = load_shp(r'YOUR_PATH\MAJOR_TOWNS.shp')
shp2 = load_shp(r'YOUR_PATH\DISTRICT_HQ.shp')
shp3 = load_shp(r'YOUR_PATH\DISTRICT_BOUNDARY.shp')
shp4 = load_shp(r'YOUR_PATH\STATE_BOUNDARY.shp')
```

### 4. Run the Script

```bash
python MAP.PY
```

### 5. Open the Output Map

```bash
start layer_map.html       # Windows
open layer_map.html        # macOS
xdg-open layer_map.html    # Linux
```

---

## ⚙️ How It Works

```
Shapefiles (.shp)
      │
      ▼
load_shp() → reads file, auto-detects CRS, reprojects to EPSG:4326
      │
      ▼
folium.Map() → initializes base map centered at [22.0°N, 78.0°E], zoom=5
      │
      ├── Layer 1: Major Towns       → CircleMarker (blue, radius=2)
      ├── Layer 2: District HQ       → CircleMarker (red, radius=3)
      ├── Layer 3: District Boundary → GeoJson (green outline)
      └── Layer 4: State Boundary    → GeoJson (black outline, weight=2)
      │
      ▼
folium.LayerControl() → adds toggle box to map
      │
      ▼
m.save("layer_map.html") → final interactive output
```

---

## 🔮 Future Improvements

- [ ] Add choropleth layer (e.g., population density or literacy rate by district)
- [ ] Include shapefiles as a download script or link to a public source
- [ ] Add a search/filter bar for towns and districts
- [ ] Export map as a static PNG via matplotlib
- [ ] Deploy as a Streamlit web app for non-technical users

---

## 🧑‍💻 Author

**Harshvardhan**
- GitHub: [@harshvardhan7709](https://github.com/harshvardhan7709)

---
