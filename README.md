# Домашнее задание к лекции «Docker Compose»

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория. 

## Задание* (необязательное)

Cделать конфигурацию docker-compose любого Вашего проекта из курса по Django, который использует БД (например, [CRUD: Склады и запасы](https://github.com/netology-code/dj-homeworks/tree/drf/3.2-crud/stocks_products)).

Результатом является `docker-compose.yml` файл с описанием конфигурации для развертывания приложения (и не забудьте про `Dockerfile`).

P.S. для создания конфигурации необходим образ своего проекта, а значит предварительно необходимо описать `Dockerfile`, сделать образ и потом уже писать `docker-compose.yml` (это типичный сценарий при работе с Docker и Docker Compose).

Созданные файлы отправьте в личном кабинете на сайте [netology.ru](https://netology.ru)

### Подсказка:

Конфигурация должна состоять из 3-х контейнеров: backend, postgres, nginx. 

Контейнеры объединяются в сеть, которые работают в связке:

- Nginx работает в качестве proxy-http для пересылки динамических запросов к Django или возвращая статические html файлы.
- PostgreSQL запускается до Django.
- Django запускается через Gunicorn.

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
