FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app/docker-compose-project/

COPY /backend/requirements.txt /app/docker-compose-project/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./backend /app/docker-compose-project/

EXPOSE 8000

CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn smart_home.wsgi -b 0.0.0.0:8000