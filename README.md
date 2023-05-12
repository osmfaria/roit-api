
## 🤖 Roit API

Este é um aplicativo de backend que recebe solicitações de robôs do UiPath. Os robôs enviam dados relacionados ao CNAE (Classificação Nacional de Atividades Econômicas) do site do IBGE, os quais podem ser armazenados e acessados por meio da API.

> O link da app deployed [API](https://roit.herokuapp.com/api/) 

> 
## 📚 Documentação 
- A documentação das rotas [aqui](https://roit.herokuapp.com/api/docs/) 
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
- Execute as migrations `python manage.py migrate` para que o banco de dados tenha o esquema criado baseado nas models.
- Finalmente, execute o comando `python manage.py runserver` a porta configurada normalmente é a 8000, verifique o applicativo rodando no `http://localhost:8000/api/doc/`
- Envie requisições para `http://localhost:8000/api/***` conforme rotas disponiveis no [docs](https://roit.herokuapp.com/api/docs/).

## 💻 Tech stack

  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" /> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /> 
  




