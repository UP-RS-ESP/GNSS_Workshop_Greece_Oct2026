import geopandas as gpd
import pandas as pd

# 1. Read CSV using pandas:
# header=0 uses line 1 as column names
# skiprows=[1] skips line 2 (the units line: 0,,,,°,°...)
df = pd.read_csv(
    "20260604-GNSS-velocity-field-Central-Greece-and-Peloponnese-Table-2.csv",
    header=0,
    skiprows=[1],
)

# 2. Convert to GeoDataFrame by setting Longitude/Latitude as geometry:
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["Longitude"], df["Latitude"]),
    crs="EPSG:4326",  # Standard WGS84 geographic coordinate system
)

# Inspect the GeoDataFrame
print(gdf.head())
print(gdf.crs)

gdf.to_file("Briole2026_GNSS_velocity.gpkg", driver="GPKG", layer="Briole2026_GNSS")
