
## 🤖 Roit API

Este é um aplicativo de backend que recebe solicitações de robôs do UiPath. Os robôs enviam dados relacionados ao CNAE (Classificação Nacional de Atividades Econômicas) do site do IBGE, os quais podem ser armazenados e acessados por meio da API.

> O link da app deployed [API](https://roit.herokuapp.com/api/) \
> A documentação das rotas [aqui](https://roit.herokuapp.com/api/docs/) 

## :toolbox: Ferramentas

- Considere utilizar [Postman](https://www.postman.com/downloads/) ou [Insomnia](https://insomnia.rest/download) para enviar requisições para a API. A documentação também permite interação com as rotas.


## 📋 Guia de instalação

- Clone este repositório;
- Para executar localmente, faz-se necessário ter o postgreSQL instalado;
- Observer o .env.exemple, crie um arquivo .env forneça as variaveis de ambiente necessárias para que o app se conecte com o database;
- Criei um ambiente virtual com `python -m venv venv`;
- Entre no ambiente virtual com `source venv/bin/activate`;
- Instale as dependências com `pip install -r requirements.txt`
- Criei as migrations com `python manage.py makemigrations`
- Execute as migrations para que o banco de dados
- Once the container is up and running, the configured port is 8000, check it running on `http://localhost:8000/api/doc/`
- Send requests `to http://localhost:8000/api/***` based on the [docs](https://court-scheduler.herokuapp.com/api/doc/).

## 💭 features

:heavy_check_mark: Email for activating new accounts;\
:heavy_check_mark: Email confirmation with static map location when scheduling a time slot in a court;\
:heavy_check_mark: Email confimation for cancelations;\
:heavy_check_mark: Add holidays, regular days off to courts.


## 💻 Tech stack

  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" /> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" /> 
  
## ER Diagram

<img src="./diagram-er.png" />

## :telescope: Upcoming updates

- [ ] Build a frontend for the application;

## :memo: License

[MIT](./LICENSE)


