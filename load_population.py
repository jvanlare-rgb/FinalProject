import geopandas as gpd

# Load your GeoJSON
gdf = gpd.read_file("../FinalProjectRepo/Data/2020population.geojson")

# Check current CRS
print(gdf.crs)

gdf = gdf.to_crs(epsg=4326)

print(gdf.crs)
gdf.to_file("Data/2020population_4326.geojson", driver="GeoJSON")
