# Desafio CorpSystem

## Desenvolver uma API Rest de controle de estoque com os seguintes módulos:
- Venda;
- Vendedor;
- Compra;
- Comprador;
- Estoque;

## Stack utilizada:

- Docker
- Python
- Django
- MySQL
- Django REST Framework

## Variáveis de ambiente

    DEBUG=True
    SECRET_KEY=arandomstring
    ALLOWED_HOSTS=*,
    DB_ENGINE=django.db.backends.mysql
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=db
    DB_PORT=3306
    RUN_PORT=8000
    RUN_HOST=0.0.0.0

## Instalação via Poetry

1. Duplicar o arquivo de variáveis de ambiente e renomealo para .env e configurar as variáveis locais
    ```sh
    cp .env.sample .env 
    ```

2. Instalar os requisitos
    ```sh
    poetry install
    ```

3. Rodar as migrações para criar as tabelas no banco de dados
    ```sh
    poetry run python manage.py migrate
    ```

4. Subir o servidor local
    ```sh
    poetry run python manage.py runserver
    ```

## Instalação via Docker

1. Fazer o build das imagens
    ```sh
    docker compose build
    ```

2. Subir os containers
    ```sh
    docker compose up
    ```

## Testes
- Rodar testes com Poetry
    ```sh
    poetry run python manage.py test --pattern="*test*.py"
    ```
- Rodar testes com Docker
    ```sh
    docker compose exec web poetry run python manage.py test --pattern="*test*.py"
    ```

# Evidências de testes

[![](https://markdown-videos-api.jorgenkh.no/youtube/8UNjDKrjlEI)](https://youtu.be/8UNjDKrjlEI)

[![](https://markdown-videos-api.jorgenkh.no/youtube/hb8Szb8fiwE)](https://youtu.be/hb8Szb8fiwE)


## Swagger do projeto

- [Swagger](http://localhost:8000/swagger/)


## DRF endpoints

- [Planos](http://localhost:8000/planos/)
- [Produtos](http://localhost:8000/produtos/)
- [Clientes](http://localhost:8000/clientes/)
- [Aportes](http://localhost:8000/planos/aportes/)
- [Resgates](http://localhost:8000/planos/aportes/)