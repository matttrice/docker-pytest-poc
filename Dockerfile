# Use an official Python runtime as a parent image
FROM python:3.8.0-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# translate local command to docker command:
# flask --app app/index run --host 0.0.0.0 --debug
CMD ["flask", "--app", "app/index", "run", "--host", "0.0.0.0", "--debug"]

# docker run -p 5000:5000 -d flask_docker