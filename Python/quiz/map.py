import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile with the Polish provinces boundaries
shp_file = "path/to/poland_provinces_shapefile.shp"
map_df = gpd.read_file(shp_file)

# Plot the map of Poland with provinces boundaries
fig, ax = plt.subplots(figsize=(10, 10))
map_df.plot(ax=ax, facecolor='lightgray')

# Add labels to provinces
for idx, row in map_df.iterrows():
    x, y = row.geometry.centroid.coords[0]
    plt.text(x, y, row.province_name, ha='center', va='center')

# Show the map
plt.show()