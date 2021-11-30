FROM python:3.8.3-slim-buster

WORKDIR /flaskapp

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV DATABASE_URL=postgresql+psycopg2://test:test@db/test
COPY . .
RUN flask db migrate && flask db upgrade
CMD ["flask", "run"]
