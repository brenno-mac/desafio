###Importação de pacotes###
import pandas as pd
from google.cloud import bigquery
from utils import google_cloud_connection, api_get_dataframe

###Conexão BigQuery###

client = google_cloud_connection()




"""EXPORTACAO
tbl_munic_exp_imp(id_munic(fk), div_exp)
"""
"""
    create table desafio.tbl_munic_exp_imp (
  id_munic int options(description='ID do município'),
  ano int options(description='Ano da análise, em YYYY, de 2015-2020'),
  tipo string options(description='Assume as opções "valor" ou "kg" para Valor FOB em US$ ou Kilogramas Líquidos'),
  exportacao_importacao string options(description='Se a linha representa uma exportação ou importação'),
  valor int options(description='Valor da importação/exportação do município'),
  CONSTRAINT id_munic FOREIGN KEY (id_munic) REFERENCES desafio.tbl_munic(id_munic) NOT ENFORCED
) options (
  description='Tabela contendo variáveis exportação e importação dos municípios'
)
"""

df_expimp = pd.read_csv('arquivos/H_EXPORTACAO_E IMPORTACAO_POR MUNICIPIO_2015-01_2020-12_DT20240807 - H_EXPORTACAO_E IMPORTACAO_POR MUNICIPIO_2015-01_2020-12_DT20240807.csv.csv')

query = """
select 
  mun.id_munic, mun.nome_munic, est.sigla_estado 
from 
  desafio.tbl_munic mun 
join 
  desafio.tbl_estado est on est.id_estado = mun.id_estado
"""

df_aux = pd.read_gbq(query=query)

df_merged = pd.merge(
    df_expimp, 
    df_aux, 
    how='left', 
    left_on=['nomeLocalidade', 'SIGLA_UF'],  
    right_on=['nome_munic', 'sigla_estado']  
)

df_merged.drop(columns=['nomeLocalidade', 'SIGLA_UF', 'nome_munic', 'sigla_estado'], inplace=True)


df_melted = pd.melt(
    df_merged, 
    id_vars=['id_munic'], 
    value_vars=[  
        'Exportação_2020_Valor US$ FOB', 'Exportação_2020_Quilograma Líquido', 
        'Importação_2020_Valor US$ FOB', 'Importação_2020_Quilograma Líquido',
        'Exportação_2019_Valor US$ FOB', 'Exportação_2019_Quilograma Líquido',
        'Importação_2019_Valor US$ FOB', 'Importação_2019_Quilograma Líquido',
        'Exportação_2018_Valor US$ FOB', 'Exportação_2018_Quilograma Líquido',
        'Importação_2018_Valor US$ FOB', 'Importação_2018_Quilograma Líquido',
        'Exportação_2017_Valor US$ FOB', 'Exportação_2017_Quilograma Líquido',
        'Importação_2017_Valor US$ FOB', 'Importação_2017_Quilograma Líquido',
        'Exportação_2016_Valor US$ FOB', 'Exportação_2016_Quilograma Líquido',
        'Importação_2016_Valor US$ FOB', 'Importação_2016_Quilograma Líquido',
        'Exportação_2015_Valor US$ FOB', 'Exportação_2015_Quilograma Líquido',
        'Importação_2015_Valor US$ FOB', 'Importação_2015_Quilograma Líquido'
    ], 
    var_name='categoria', 
    value_name='valor'  
)


df_melted['ano'] = df_melted['categoria'].str.extract(r'(\d{4})')
df_melted['tipo'] = df_melted['categoria'].apply(
    lambda x: 'valor' if 'Valor US$ FOB' in x else 'kg'
)
df_melted['exportacao_importacao'] = df_melted['categoria'].apply(
    lambda x: 'exportacao' if 'Exportação' in x else 'importacao'
)

df_final = df_melted[['id_munic', 'ano', 'tipo', 'exportacao_importacao', 'valor']]

df_final['ano'] = df_final['ano'].astype(int)

# client.load_table_from_dataframe(dataframe = df_final, destination='desafio.tbl_munic_exp_imp')
