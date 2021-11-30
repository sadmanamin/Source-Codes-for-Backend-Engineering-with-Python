FROM python:3.8.3-slim-buster
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --upgrade pip
RUN pip install flask gunicorn
COPY . .
CMD ["gunicorn","--workers","8","app:app"]


