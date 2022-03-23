# %%
import numpy as np
import pandas as pd
import plotly.express as px
import geopandas as gpd
import streamlit as st

# %%
zctas = gpd.read_file('./data/montgomery_zip_vars.geojson')

# %%
zctas.set_index('GEOID', inplace = True)

# %%
# zctas.plot()

# %%
# columns = zctas.columns
selectable_cols = ['tot_popE', 'hispanicE', 'nh_whiteE', 'nh_blackE', 'nh_aianE',
       'nh_asianE', 'nh_pacislanderE', 'non_citizenE', 'hispanicE_share',
       'nh_whiteE_share', 'nh_blackE_share', 'nh_aianE_share',
       'nh_asianE_share', 'nh_pacislanderE_share', 'non_citizenE_share',
       'over55', 'disability_est', 'mhi']
selected_col = st.selectbox('Demographic', selectable_cols)

opacities = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
selected_opacity = st.selectbox('Opacity', opacities, index=2)

# %%
fig = px.choropleth_mapbox(zctas, 
    geojson=zctas.geometry,
    locations=zctas.index, 
    color=selected_col,
    center={"lat": 40.1718, "lon": -75.3175},
    opacity=selected_opacity,
    mapbox_style="open-street-map",
    zoom=8.9
    )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

# %%
st.plotly_chart(fig, use_container_width=True)
