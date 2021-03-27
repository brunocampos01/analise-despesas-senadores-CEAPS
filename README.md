# Análise de dados dos gastos públicos dos Senadores
[![Python 3](https://img.shields.io/badge/Python-3-yellow.svg)](https://www.python.org/downloads/release/python-391/)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

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
.
├── data
│   ├── cleansing
│   │   ├── dados_limpos_ceaps_cleansing.csv
│   │   └── map_senadores.csv
│   └── dumps
│       ├── 2008.csv
│       ├── 2009.csv
│       ├── 2010.csv
│       ├── 2011.csv
│       ├── 2012.csv
│       ├── 2013.csv
│       ├── 2014.csv
│       ├── 2015.csv
│       ├── 2016.csv
│       ├── 2017.csv
│       ├── 2018.csv
│       └── 2019.csv
├── notebooks
│   ├── 01-prepare-environment-and-data-acquisition.ipynb
│   ├── 02-data-cleaning.ipynb
│   └── 03-data-exploration.ipynb
├── README.md
├── references
│   └── senado.jpg
└── src
    ├── dump_data.py
    ├── environment
    │   ├── config_environment.txt
    │   ├── container
    │   │   └── Dockerfile
    │   ├── create_requirements.sh
    │   ├── create_virtual_env.sh
    │   ├── __init__.py
    │   ├── jupyter_notebook_config.py
    │   ├── makefile
    │   ├── prepare_env.py
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── show_config_environment.sh
    │   ├── show_struture_project.sh
    │   ├── struture_project.txt
    │   ├── test_environment.py
    │   ├── venv
    │   └── virtualenv_requirements.txt
    ├── __init__.py
    └── visualization
        └── matplotlib_config.ini

10 directories, 37 files
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

<p  align="left">
<br/>
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/email.png" alt="Gmail" width="30">
</a>
<a href="https://stackoverflow.com/users/8329698/bruno-campos" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/stackoverflow.png" alt="GitHub" width="30">
</a>
<a href="https://www.linkedin.com/in/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" alt="LinkedIn" width="30"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/github.png" alt="GitHub" width="30"></a>
<a href="https://brunocampos01.netlify.app/" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/blog.png" alt="Website" width="30">
</a>
<a href="https://medium.com/@brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/medium.png" alt="GitHub" width="30">
</a>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png",  align="right" /></a><br/>
</p>
