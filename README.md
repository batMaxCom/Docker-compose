# Развертка проекта
Необходимо создать файл .env в директории backend, по примеру:
```
SECRET_KEY='you_secret_key'
ALLOWED_HOSTS=*
DEBUG=True
DB_ENGINE=django.db.backends.postgresql
DB_HOST=postgresdb
DB_NAME='you_db_name'
DB_USER=you_'you_postgre_username'
DB_PASSWORD='you_postgre_password'
```
Также данные для БД необходимо заполнить в файле docker-compose.yml (в строках 9, 10, 11)
```
POSTGRES_DB: 'you_db_name'
POSTGRES_USER: 'you_postgre_username'
POSTGRES_PASSWORD: 'you_postgre_password'
```
Для развертки проекта введите коману:
```
docker-compose up -d
```