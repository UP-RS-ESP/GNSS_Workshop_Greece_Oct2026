# INITIATE: GNSS Workshop - Greece September / October 2026

If you **DO NOT** have a conda environment with relevant packages, please install this:
```bash
conda create -n GNSSdata -c conda-forge python ipython geopandas pandas numpy pygmt scipy rasterio ipython jupyterlab rioxarray cartopy matplotlib
conda activate GNSSdata
ipython kernel install --user --name=GNSSdata
jupyter lab
```

If you have a working environment, you likely only need to install `pygmt`, `rasterio`, `geopandas`, and `cartopy`:
```bash
conda install -c conda-forge geopandas pygmt rasterio rioxarray cartopy
```

For the GNSS data analysis of Corinth, please download the Copernicus 30 m available here (this is needed for the Jupyter Lab Exercise): 
https://www.dropbox.com/scl/fi/6vs1rsboy9aq0ivnzw6a4/COP30_Greece_epsg4326.tif?rlkey=uasuhfiq164h2djoxnqyr0lc1&st=fbfilqcq&dl=0

This was generate with [sardem](https://github.com/scottstanie/sardem). This short script also compressed the TIF using gdal: 
```bash
sardem --bbox 19 35 26 40 -o COP30_Greece_epsg4326.tif
gdal_translate COP30_Greece_epsg4326.tif COP30_Greece_epsg4326b.tif -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=3
mv COP30_Greece_epsg4326b.tif COP30_Greece_epsg4326.tif
```

There are three Folder with different exercises that calculate spatial derivatives from GNSS data using different approaches:
1. Synthetic GNSS Data to explore the calculation of spatial gradients, including dilatation, compression,
2. Briole et al. 2026: *The GNSS velocity field of central Greece and the Peloponnese*
    - Extentive and curated dataset for the Gulf of Cornith
    - https://academic.oup.com/gji/article/246/3/ggag230/8707067?login=false&utm_source=researchgate.net&utm_medium=article
3. Steffen et al., 2025: *EuVeM2022—a European three-dimensional GNSS velocity model based on least-squares collocation*
    - https://academic.oup.com/gji/article/241/1/437/8006706

