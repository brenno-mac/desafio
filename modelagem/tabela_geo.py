###Importação de pacotes###
import geopandas as gpd
from google.cloud import bigquery
from utils import google_cloud_connection, api_get_dataframe

###Conexão BigQuery###

client = google_cloud_connection()


"""DADOS GEOGRAFICOS
tbl_munic_geo(id_munic(fk), area_km2, coord)
"""
"""
create table desafio.tbl_munic_geo (
  id_munic int options(description='ID do município'),
  area_km2 float64 options(description='Área em km² do município'),
  coordenada geography options(description='Latitude e longitude do município'),
  CONSTRAINT id_munic FOREIGN KEY (id_munic) REFERENCES desafio.tbl_munic(id_munic) NOT ENFORCED
) options (
  description='Tabela contendo variáveis de geolocalização e tamanho do município'
)
"""

df_geo = gpd.read_file('arquivos/municipios.geojson')

df_geo.drop(columns=['NM_MUN', 'SIGLA_UF'], inplace=True)

df_geo.rename(columns={'CD_MUN':'id_munic', 'AREA_KM2':'area_km2', 'geometry':'coordenada'}, inplace=True)

df_geo['id_munic'] = df_geo['id_munic'].astype(int)

# client.load_table_from_dataframe(dataframe = df_geo, destination='desafio.tbl_munic_geo')

