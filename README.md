# DataScience JOBS Prediction

## Descrição

Este é um Data App para predição para DataScience Jobs

Desenvolvido pelos alunos: Andrea Monicque, Francisco Marcelo, Lucas Pereira e Marcos Wenneton para a discplina de Infraestrutura em Nuvem para Projetos com Ciência dos Dados do curso de Pós-Graduação em Ciência de Dados da Universidade do Estado do Amazonas - UEA.

### Dataset e Modelo Preditivo
O dataset utilizado está disponível gratuitamente na plataforma Kaggle por este [link]().

## Requerimentos
Para executar localmente, é necessário você ter instalado as seguintes ferramentas:
- [Python 3](https://www.python.org/downloads/)
- [PIP](https://docs.python.org/3/installing/index.html)

Após isso você pode clonar o repositório com o comando:
```
git clone https://github.com/llucasreis/streamlit-webapp
```

## Iniciando a aplicação

Antes de iniciar é recomendável você utilizar um ambiente virtual, e para isto, execute os seguintes comandos:
```shell
# instalando a biblioteca de ambiente virtual
pip install virtualenv

# criando o ambiente virtual
python3 -m virtualenv .venv

# ativando o ambiente virtual
source .venv/bin/activate
```

Após ativar seu ambiente virtual, basta executar o comando para instalar as bibliotecas:
```shell
pip install -r requirements.txt
```

E por fim, execute o comando para rodar a aplicação com `streamlit`:
```shell
streamlit run src/app.py
```

---

Made by [Andrea Monicque](https://github.com/DevNicque), [Francisco Marcelo](https://github.com/fmmdamasceno), [Lucas Pereira](https://github.com/llucasreis) and [Marcos Wenneton](https://github.com/wenneton)