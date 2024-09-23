###Importação de pacotes###
import pandas as pd
from google.cloud import bigquery
from utils import google_cloud_connection, api_get_dataframe

###Conexão BigQuery###

client = google_cloud_connection()



"""TABELA_MUNICIPIOS
tbl_munic(id_munic(pk), nome_munic, id_estado(fk))
"""
"""
  create table desafio.tbl_munic (
  id_munic int options(description='ID do município'),
  nome_munic string options(description='Nome do município'),
  id_estado int options(description='ID do estado - chave secundária'),
  primary key (id_munic) not enforced,
  CONSTRAINT id_estado FOREIGN KEY (id_estado) REFERENCES desafio.tbl_estados(id_estado) NOT ENFORCED
) options (
  description='Tabela contendo municípios e estado dos municípios'
)
    """

###Requisição da API do IBGE###
url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

df_munic = api_get_dataframe(url)

###Filtrando colunas relevantes###
df_munic = df_munic[['id', 'nome', 'microrregiao.mesorregiao.UF.sigla', 'regiao-imediata.regiao-intermediaria.UF.regiao.nome']]

df_munic = pd.merge(df_munic, df_estado[['sigla_estado', 'id_estado']], left_on='microrregiao.mesorregiao.UF.sigla', right_on='sigla_estado', how = 'left')

df_munic.drop(columns=['microrregiao.mesorregiao.UF.sigla', 'regiao-imediata.regiao-intermediaria.UF.regiao.nome', 'sigla_estado'], inplace=True)

df_munic.rename(columns={'id':'id_munic', 'nome':'nome_munic'}, inplace=True)

# client.load_table_from_dataframe(dataframe = df_munic, destination='desafio.tbl_munic')
