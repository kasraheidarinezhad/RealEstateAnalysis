import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium 

gdf = gpd.read_file('C:/Users/admin/Downloads/canada.geojson')

m = folium.Map(location=[48, -102], zoom_start=3)   # Create the map object


folium.GeoJson(gdf).add_to(m)  # Add the GeoJSON data to the map

# Display the map
m