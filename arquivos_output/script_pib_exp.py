import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

###PIB X EXPORTACAO

query_pibexp = """
select 
  dem.id_munic,
  dem.pib_munic, 
  imp.valor as exportacao
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic_exp_imp imp on imp.id_munic = dem.id_munic and imp.ano = 2020 and imp.tipo = 'valor' and imp.exportacao_importacao = 'exportacao'
"""

df_aux = pd.read_gbq(query=query_pibexp)


plt.figure(figsize=(10, 6))
sns.scatterplot(x='pib_munic', y='exportacao', data=df_aux, hue='id_munic', s=100)

plt.title('Relação entre PIB e Exportação dos Municípios', fontsize=14)
plt.xlabel('PIB (em milhões)', fontsize=12)
plt.ylabel('Exportação (em milhões)', fontsize=12)

plt.savefig("pibxexportacao.png")  




### NOVO GRÁFICO SEM OUTLIERS DO PIB

Q1 = df_aux['pib_munic'].quantile(0.25)
Q3 = df_aux['pib_munic'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_sem_outliers = df_aux[(df_aux['pib_munic'] >= limite_inferior) & (df_aux['pib_munic'] <= limite_superior)]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='pib_munic', y='exportacao', data=df_sem_outliers, hue='id_munic', s=100)

plt.title('Relação entre PIB e Exportação dos Municípios (Sem Outliers)', fontsize=14)
plt.xlabel('PIB (em milhões)', fontsize=12)
plt.ylabel('Exportação (em milhões)', fontsize=12)

plt.savefig("pibxexportacao_sem_outliers.png")
