# %%
import plotly.express as px
import geopandas as gpd
import streamlit as st

# %%
zctas = gpd.read_file('./data/eldernet_big_combined.geojson')

# %%
rename_cols = {
    'tot_popE': 'tot_population',
    'hispanicE': 'tot_hispanic',
    'nh_whiteE': 'tot_white',
    'nh_blackE': 'tot_black',
    'nh_aianE': 'tot_AmInd',
    'nh_asianE': 'tot_asian',
    'nh_pacislanderE': 'tot_pac_islander',
    'non_citizenE': 'tot_non_citizen',
    'hispanicE_share': 'hispanic_share',
    'nh_whiteE_share': 'white_share',
    'nh_blackE_share': 'black_share',
    'nh_aianE_share': 'AIan_share',
    'nh_asianE_share': 'asian_share',
    'nh_pacislanderE_share': 'pac_islander_share',
    'non_citizenE_share': 'non_citizen_share',
    'over55': 'tot_over55',
    'disability_est': 'tot_disability',
    'mhi': 'median_household_income',
    'Total': 'tot_E_clients',
    'CM': 'E_Care_Mgmt',
    'Pantry': 'E_Pantry',
    'Volunteer': 'E_Volunteer',
    'over55_share': 'over55_share',
    'disabled_share': 'disability_share',
    'over55_z': 'over55_zscore',
    'disabled_z': 'disability_zscore',
    'service_cat': 'E_serviced_zip' 
}
zctas.rename(rename_cols, axis='columns', inplace=True)

# %%
zctas.set_index('NAME', inplace = True)

# %%
# zctas.plot()

# %%
st.title('Geographic visualization for Eldernet')
st.text('Census data utilized is estimated by the census')

# %%
st.set_page_config(layout='wide')
columns = zctas.columns
selectable_cols = [
    'tot_population',
    'tot_hispanic',
    'tot_white',
    'tot_black',
    'tot_AmInd',
    'tot_asian',
    'tot_pac_islander',
    'tot_non_citizen',
    'hispanic_share',
    'white_share',
    'black_share',
    'AIan_share',
    'asian_share',
    'pac_islander_share',
    'non_citizen_share',
    'tot_over55',
    'tot_disability',
    'median_household_income',
    'tot_E_clients',
    'E_Care_Mgmt',
    'E_Pantry',
    'E_Volunteer',
    'over55_share',
    'disability_share',
    'over55_zscore',
    'disability_zscore',
    'E_serviced_zip'
]
selected_col = st.selectbox('Census/Eldernet data', selectable_cols)

opacities = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
selected_opacity = st.selectbox('Opacity', opacities, index=2)

# %%
fig = px.choropleth_mapbox(zctas, 
    geojson=zctas.geometry,
    locations=zctas.index, 
    color=selected_col,
    center={"lat": 40.1369, "lon": -75.5248},
    opacity=selected_opacity,
    mapbox_style="open-street-map",
    zoom=8.1
    )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

# %%
st.plotly_chart(fig, use_container_width=True)
