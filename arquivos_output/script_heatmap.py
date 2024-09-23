import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap


### GRÁFICO DE CALOR DE PRODUTIVIDADE

query_produtividade_coordenada = """select 
  dem.id_munic,
  dem.produtividade,
  geo.coordenada 
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic_geo geo on geo.id_munic = dem.id_munic
where 
  dem.produtividade is not null
"""

df_aux = pd.read_gbq(query=query_produtividade_coordenada)


def extract_lat_lon(coordenada):
    coordenada = coordenada.replace('POINT(', '').replace(')', '')
    lon, lat = map(float, coordenada.split())
    return lat, lon

df_aux[['latitude', 'longitude']] = df_aux['coordenada'].apply(lambda x: pd.Series(extract_lat_lon(x)))

# Centralizando no Brasil
m = folium.Map(location=[-15.7801, -47.9292], zoom_start=4)  

heat_data = [[row['latitude'], row['longitude'], row['produtividade']] for index, row in df_aux.iterrows()]

HeatMap(heat_data, radius=15, max_zoom=13).add_to(m)

m.save("mapa_de_calor_produtividade.html")
