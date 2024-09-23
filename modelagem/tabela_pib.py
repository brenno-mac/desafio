###Importação de pacotes###
import pandas as pd
from google.cloud import bigquery
from utils import google_cloud_connection, api_get_dataframe

###Conexão BigQuery###

client = google_cloud_connection()



"""PIB
tbl_munic_demographics(id_munic(fk), pop_res, pib_munic, produtividade)
"""
"""
    create table desafio.tbl_munic_demographics (
  id_munic int options(description='ID do município'),
  pop_res int options(description='População residente do município'),
  pib_munic float64 options(description='PIB do município * 1000'),
  produtividade float64 options(description='Produtividade do município, calculada como pib_munic/pop_res'),
  CONSTRAINT id_munic FOREIGN KEY (id_munic) REFERENCES desafio.tbl_munic(id_munic) NOT ENFORCED
) options (
  description='Tabela contendo variáveis de demografia dos municípios'
)
    """

df_demo = pd.read_csv('arquivos/demografia_municipios_2017.csv')

###Filtrando colunas relevantes
df_demo = df_demo[['CD_MUN', 'NM_MUN', 'População residente', 'PIB Municipal']]

###Transformando coluna de população residente para número
df_demo['População residente'] = df_demo['População residente'].str.replace('"', '').astype(float)

###Após analisar as colunas e identificar valores negativos em algumas linhas de população residente, mas que faziam sentido
df_demo['População residente'] = df_demo['População residente'].abs()

###Criando coluna de produtividade, conforme especificado
df_demo['produtividade'] = df_demo['PIB Municipal']/df_demo['População residente']

df_demo.drop(columns=['NM_MUN'], inplace=True)

df_demo['População residente'].fillna(0).astype(int).replace(0, None)

df_demo.rename(columns={'CD_MUN':'id_munic', 'População residente':'pop_res', 'PIB Municipal':'pib_munic'}, inplace=True)

client.load_table_from_dataframe(dataframe = df_demo, destination='desafio.tbl_munic_demographics')
