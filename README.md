
## 🤖 Roit API

Este é um aplicativo de backend que recebe solicitações de robôs do UiPath. Os robôs enviam dados relacionados ao CNAE (Classificação Nacional de Atividades Econômicas) do site do IBGE, os quais podem ser armazenados e acessados por meio da API.

> O link da app que está disponível em produção no heroku [API](https://roit.herokuapp.com/api/docs/) 

> 
## 📚 Documentação 
- A documentação das rotas [aqui](https://roit.herokuapp.com/api/docs/) 
## :toolbox: Ferramentas

- Considere utilizar [Postman](https://www.postman.com/downloads/) ou [Insomnia](https://insomnia.rest/download) para enviar requisições para a API. A documentação também permite interação com as rotas.


## 📋 Guia de instalação
Para executar localmente este app, siga as intruções abaixo:

- Clone este repositório;
- Para executar localmente, certifique-se de ter o PostgreSQL instalado em seu sistema;
- Observe o arquivo .env.example e crie um arquivo chamado .env, fornecendo as variáveis de ambiente necessárias para que o aplicativo possa se conectar ao banco de dados;
- Crie um ambiente virtual executando o comando `python -m venv venv`;
- Ative o ambiente virtual executando o comando `source venv/bin/activate`;
- Instale as dependências com o comando `pip install -r requirements.txt`
- Crie as migrações usando `python manage.py makemigrations`;
- Execute as migrações para criar o esquema do banco de dados baseado nas models, utilizando o comando `python manage.py migrate`;
- Finalmente, execute o comando `python manage.py runserver` a porta configurada normalmente é a 8000, verifique o applicativo rodando no `http://localhost:8000/api/doc/`
- Finalmente, inicie o servidor com o comando `python manage.py runserver`. Normalmente, o aplicativo estará disponível em `http://localhost:8000/`. Verifique a documentação da API em [docs](https://roit.herokuapp.com/api/docs/). para obter as rotas disponíveis. Envie as requisições para `http://localhost:8000/api/***` de acordo com a rota desejada. 

## 💻 Tech stack

  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" /> <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" /> 
  




