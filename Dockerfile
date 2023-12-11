FROM python:3.8

WORKDIR /app

COPY server/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY server/ .

CMD ["gunicorn", "flask_app:app", "-c", "gunicorn_config.py"]
