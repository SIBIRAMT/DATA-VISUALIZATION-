# -*- coding: utf-8 -*-
"""path.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dKB0Pgpe0n2h0oTfwdVJXumkChg1Itzr
"""

import geopandas as gpd
import folium

# Load GeoJSON data into a GeoDataFrame
file_path = "/content/sibi2.geojson"
gdf = gpd.read_file(file_path)

# Create a Folium map centered around Tokyo
tokyo_map = folium.Map(location=[35.6895, 139.6917], zoom_start=12)

# Add GeoJSON layer to the map
folium.GeoJson(gdf).add_to(tokyo_map)

# Sample locations for markers (latitude, longitude)
marker_locations = [
    (35.6895, 139.6917),  # Tokyo Station
    (35.6894, 139.6920),  # Sample Location 1
    (35.6896, 139.6915),  # Sample Location 2
]

# Add red markers to the map
for location in marker_locations:
    folium.Marker(location=location, icon=folium.Icon(color='red')).add_to(tokyo_map)

# Display the map directly in the Jupyter Notebook
tokyo_map

pip install geopandas matplotlib

import geopandas as gpd
import matplotlib.pyplot as plt

# Load pedestrian paths GeoJSON file
file_path = "/content/sibi2.geojson"
pedestrian_data = gpd.read_file(file_path)

# Data Preprocessing (you may need to perform additional steps based on your specific dataset)

# Spatial Analysis

# Walkability Metrics

# Visualization

# Example: Pie chart of walkability categories
walkability_categories = ['Low', 'Medium', 'High']
walkability_counts = [100, 250, 150]  # Replace with your actual data

plt.figure(figsize=(8, 8))
plt.pie(walkability_counts, labels=walkability_categories, autopct='%1.1f%%', startangle=140)
plt.title('Walkability Categories in Tokyo')
plt.show()

# Example: Bar chart of walkability scores by neighborhood
neighborhoods = pedestrian_data['neighborhood']  # Replace with your actual neighborhood column
walkability_scores = pedestrian_data['walkability_score']  # Replace with your actual walkability score column

plt.figure(figsize=(12, 6))
plt.bar(neighborhoods, walkability_scores, color='skyblue')
plt.xlabel('Neighborhoods')
plt.ylabel('Walkability Score')
plt.title('Walkability Scores by Neighborhood in Tokyo')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()