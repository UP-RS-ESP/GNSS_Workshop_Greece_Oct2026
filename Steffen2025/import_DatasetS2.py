import geopandas as gpd
import pandas as pd

# 1. Read whitespace-delimited file
# sep=r'\s+' matches 1 or more spaces/tabs
column_names = ["lon", "lat", "Ve", "Vn", "Se", "Sn", "Vu", "Su", "site", "t1", "t2"]
df = pd.read_csv("DatasetS2", sep=r"\s+", names=column_names, skiprows=1)

# 2. Clean column names (strip leading '*' or whitespace)
df.columns = df.columns.str.lstrip("*").str.strip()

# 3. Create GeoDataFrame (keeping lon/lat as attribute columns too)
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df["lon"], df["lat"]),
    crs="EPSG:4326",  # Standard WGS 84
)

# 4. Export to GeoPackage
gdf.to_file(
    "Steffen2025_DatasetS2_epsg4326.gpkg", driver="GPKG", layer="Steffen2025_velocity"
)

# Inspect the result
print(gdf.info())
print(gdf.head())
