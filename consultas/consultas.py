###Consultas de query feitas na base 



###MAIOR PIB DE TOCANTINS###

"""
with ranking_pib_tocantins as 
(select 
  dem.id_munic, 
  dem.pib_munic,
  mun.nome_munic,
  est.nome_estado,
  ROW_NUMBER() OVER (ORDER BY dem.pib_munic DESC) AS posicao_pib
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic mun on mun.id_munic = dem.id_munic
join 
  desafio.tbl_estado est on est.id_estado = mun.id_estado
where 
  est.sigla_estado = 'TO' ) 
select 
  * 
from 
  ranking_pib_tocantins
where posicao_pib between 1 and 5
  """
  
  
  
###MENOR PIB DE SP###

"""
with ranking_pib_sp as 
(select 
  dem.id_munic, 
  dem.pib_munic,
  mun.nome_munic,
  est.nome_estado,
  ROW_NUMBER() OVER (ORDER BY dem.pib_munic ASC) AS posicao_pib
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic mun on mun.id_munic = dem.id_munic
join 
  desafio.tbl_estado est on est.id_estado = mun.id_estado
where 
  est.sigla_estado = 'SP' ) 
select 
  * 
from 
  ranking_pib_sp
where posicao_pib between 1 and 5
  """
  
  
  
###ESTADOS MAIS PRODUTIVOS

"""
  select 
  est.nome_estado,
  round(sum(dem.produtividade),2) as produtividade_estadual
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic mun on mun.id_munic = dem.id_munic
join 
  desafio.tbl_estado est on est.id_estado = mun.id_estado
group by
  est.nome_estado
order by 
  round(sum(dem.produtividade),2) desc
  """
  
  
###REGIOES MAIS PRODUTIVAS

"""
  select 
  est.regiao,
  round(sum(dem.produtividade),2) as produtividade_regional
from 
  desafio.tbl_munic_demographics dem
join 
  desafio.tbl_munic mun on mun.id_munic = dem.id_munic
join 
  desafio.tbl_estado est on est.id_estado = mun.id_estado
group by
  est.regiao
order by 
  round(sum(dem.produtividade),2) desc
  """
 