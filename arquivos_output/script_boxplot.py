import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



###BOXPLOT PIB POR REGIAO###

query_boxplot = """
select 
  est.regiao,
  dem.produtividade
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic mun on mun.id_munic = dem.id_munic
join 
  desafio.tbl_estado est on est.id_estado = mun.id_estado
"""

df_aux = pd.read_gbq(query=query_boxplot)

plt.figure(figsize=(8, 6))
sns.boxplot(x='regiao', y='produtividade', data=df_aux)

# Adicionar títulos e labels
plt.title('Boxplot de Produtividade por Região')
plt.xlabel('Região')
plt.ylabel('Produtividade')

plt.savefig("boxplot_produtividade.png")
