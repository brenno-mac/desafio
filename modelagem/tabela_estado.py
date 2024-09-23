###Importação de pacotes###
import pandas as pd
from google.cloud import bigquery
from utils import google_cloud_connection, api_get_dataframe

###Conexão BigQuery###

client = google_cloud_connection()



"""TABELA_ESTADOS
tbl_estado(id_estado(pk), nome_estado, regiao)
"""
"""
    create table desafio.tbl_estado (
  id_estado int options(description='ID do estado'),
  sigla_estado string options(description='Sigla do estado'),
  nome_estado string options(description='Nome do estado'),
  regiao string options(description='Região do país a qual o estado pertence'),
  primary key (id_estado) not enforced 
) options (
  description='Tabela contendo estados e região dos estados'
)
    """

url_estado = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'

df_estado = api_get_dataframe(url_estado)

df_estado.drop(columns=['regiao.id', 'regiao.sigla'], inplace=True)

df_estado.rename(columns={'id':'id_estado', 'sigla':'sigla_estado', 'nome':'nome_estado', 'regiao.nome':'regiao'}, inplace=True)

# client.load_table_from_dataframe(dataframe = df_estado, destination='desafio.tbl_estado')

