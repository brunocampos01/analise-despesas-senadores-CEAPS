# Análise de dados dos gastos públicos dos Senadores
[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/downloads/release/python-371/)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/452bbb3d75024f76a8c81a98e7bf73b4)](https://www.codacy.com/app/brunocampos01/learning-data-science?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=brunocampos01/learning-data-science&amp;utm_campaign=Badge_Grade)

## Describe project

![Image of Yaktocat](https://upload.wikimedia.org/wikipedia/pt/0/09/Senado_Federal_do_Brasil.png)

O objetivo é explorar os dados públicos afim de aplicar as técnicas de data science. Foi realizado as seguintes etapas:

1. Levantamento de Questões
  - Qual o senador que mais gastou ?
  - Qual o senador que mais pediu reembolso?
  - Reembolsos menores que R$ 1,00
  - Gráfico comparando a quantidade gasta por cada senador
  - Gráfico de gastos mensais dividido por tipo de gasto

2. Análise dos Metadados
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


## Datasource
As bases de dados: https:/www12.senado.leg.br/transparencia/dados-abertos-transparencia/dados-abertos-ceaps

## Quickstart
1. [Prepare environment and Data Acquisition](notebooks/)
1. [Data Cleaning](notebooks/)
2. [Data Exploration](notebooks/)

## Struture this Project
```
```

## Requirements
- Python 3.7.3 or more
```sh
sudo apt-get install Python3.7.3
```

- pip
```
sudo apt-get install python3-pip
```

- Python Virtual Environment
```sh
pip3 install --user virtualenv==16.6.0
```

- Git
```sh
sudo apt-get install git
```

## Running
1. Clone this repository
```sh
git clone https://github.com/brunocampos01/challenge-keyrus
cd challenge-keyrus
```

2. Choose which environment to running
 - [local](src/environment/README.md)
 - [virtual environment](src/environment/README.md)
 - [container](src/environment/README.md)

3. In terminal running command `jupyter-notebook` and navigate in this repository: `notebooks`

##### NOTES
- All the development was done using **virtualenv**. 
- To learn more about the environment that has been developed, access the file [config_environment.txt](src/environment/config_environment.txt)

---

## Author
- Bruno Aurélio Rôzza de Moura Campos (brunocampos01@gmail.com)

## Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Bruno A. R. M. Campos</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
