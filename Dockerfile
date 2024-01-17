# Use an official Python runtime as a parent image
FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

#  flask --app app/index run --host 0.0.0.0 --debug
CMD ["flask", "--app", "app/index", "run", "--host", "0.0.0.0", "--debug"]