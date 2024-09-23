import pandas as pd

###CSV###

query_csv = """
select 
  mun.nome_munic as `Nome do município`, 
  est.nome_estado as Estado,
  est.regiao as `Região`, 
  dem.pib_munic as PIB, 
  imp.valor as `Valores de importação 2020`,
  expo.valor as `Valores de exportação 2020`
from 
  desafio.tbl_munic mun
left join
  desafio.tbl_estado est on est.id_estado = mun.id_estado
left join 
  desafio.tbl_munic_demographics dem on dem.id_munic = mun.id_munic
left join 
  desafio.tbl_munic_exp_imp imp on imp.id_munic = mun.id_munic and imp.ano = 2020 and imp.tipo = 'valor' and imp.exportacao_importacao = 'importacao'
left join 
  desafio.tbl_munic_exp_imp expo on expo.id_munic = mun.id_munic and expo.ano = 2020 and expo.tipo = 'valor' and expo.exportacao_importacao = 'exportacao'"""

df_aux = pd.read_gbq(query=query_csv)

df_aux.to_csv('csvpedido.csv')




