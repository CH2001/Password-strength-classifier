FROM python:3.10.0-slim

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pipenv install --deploy --ignore-pipfile

COPY model.py model.bin /app/

EXPOSE 8081

CMD ["pipenv", "run", "waitress-serve", "--port=8081", "model:app"]
