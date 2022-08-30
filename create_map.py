import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
import mapclassify
import folium

class CreateMap():
    def __init__(self):
        # COUNTRIES = gpd.read_file(r"test_files\countries.geojson")
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

        m = folium.Map(location=[48, -102], zoom_start=3)

        folium.Choropleth(
            geo_data=world,
            data=world,
            columns=["continent", "name"],
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.2,
        ).add_to(m)

        folium.LayerControl().add_to(m)
        m.save('templates/map.html')
