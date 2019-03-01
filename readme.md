# Análise de dados dos gastos públicos dos Senadores
[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/downloads/release/python-371/)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)


## Describe project 

<img src="images/senado.jpg"height="50%" width="50%"/>

O objetivo é explorar os dados públicos afim de aplicar as técnicas de data science. Foi realizado as seguintes etapas:

- 1 STEP) Questions
  - Qual o senador que mais gastou ?
  - Qual o senador que mais pediu reembolso?
  - Reembolsos menores que R$ 1,00
  - Gráfico comparando a quantidade gasta por cada senador 
  - Gráfico de gastos mensais dividido por tipo de gasto

- 2 STEP) Data Acquisition
  - Fonte: portal da transparência: https:/www12.senado.leg.br/transparencia/dados-abertos-transparencia/dados-abertos-ceaps
  - Ano: 2016
  - Format: CSV

- 3 STEP) Data analysis
```
Notas:
Os dados estão com formato de ;
Coluna SENADOR é o target
Há 10 colunas
26691 linhas
A data com maior número de pedido de reembolso foi 01/06/2016, por quê?
Analisando as variáveis que temos para trabalhar é possível notar que será necessário converter algumas colunas de String para tipo numérico e assim conseguir aplicar alguma técnica de análise.
É possível ter valores missing pois nem todas as colunas tem o mesmo número de linhas.
Analisar o SENADOR 90, pois é quem masi teve pedidos de reembolso nesse ano.
```
- 4 STEP) Data Cleanning
  - Types convert
  - Check outliers
  - Check missing values
  - Check unique values
  - Check duplicate
  - Check irrelevant data

- Segunda Parte
  - Views

## Pre Requirements
 - Python 3.7.1 or more:<br/>	
 `sudo apt install python3.7`	
 - pip:<br/>	
 `sudo apt install python-pip`	
 - Libraries:<br/>	
 `pip install -r requirements.txt`<br/>	

## Quickstart
https://github.com/brunocampos01/analise-despesas-senadores-CEAPS/blob/master/analise-exploratoria-CEAPS-2016-part01.ipynb

Parte 02:
https://github.com/brunocampos01/analise-despesas-senadores-CEAPS/blob/master/analise-exploratoria-CEAPS-2016-part01.ipynb


## References 
- https://www12.senado.leg.br/transparencia/dados-abertos-transparencia/dados-abertos-ceaps

## How to contribuite
- [x] Fork the repository.
- [x] Create a topic branch.
- [x] *Implement your feature or bug fix.*
- [x] Add, commit, and **push** your changes.
- [x] Submit a pull request.

## Author
- Bruno Aurélio Rôzza de Moura Campos (brunocampos01@gmail.com)
## Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Bruno A. R. M. Campos</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.