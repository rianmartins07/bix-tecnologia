# Configuração do Ambiente

1. Inicie criando um ambiente de desenvolvimento:
    **python -m venv venv**


2. Instale as dependências do projeto:
    **pip install -r requirements.txt**


# Configuração do Banco de Dados

1. Crie um banco de dados no PostgreSQL utilizando o pgAdmin. Configure o endereço, porta e usuário conforme necessário.

2. Crie um arquivo `.env` a partir do `.env.example`, alterando as informações de acordo com as configurações locais.

3. Com o banco criado e o `.env` configurado corretamente, realize as tratativas e migrações do banco:

## Migrando as configurações do banco de dados:# Configuração do Ambiente

1. Inicie criando um ambiente de desenvolvimento:
    **python manage.py migrate**


## Rodando as fixtures (dados para dentro do banco de dados):
    python manage.py loaddata fixture/imoveis.json;
    python manage.py loaddata fixture/plataformas.json;
    python manage.py loaddata fixture/anuncios.json;
    python manage.py loaddata fixture/reserva.json;


# Executando o Servidor

Para rodar o servidor e garantir seu correto funcionamento:
    **python manage.py runserver**


## Acesse o domínio da aplicação que será exibido no terminal e visite o seguinte URL:
    http://seu_dominio.com/api/
    Ou
    http://seu_dominio.com/redoc/


Neste endereço, você terá acesso a todas as interfaces de consumo, criação, alteração e deleção de dados de acordo com o estabelecido no arquivo.

# Testes Automatizados

    Para realizar os testes automatizados, utilize o seguinte comando:
    python manage.py test

**É de suma importância rodar esse comando de teste toda a vez que for realizado alguma feature/fix no projeto.**



celery -A bix beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler