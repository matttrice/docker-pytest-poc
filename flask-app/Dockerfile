# Use an official Python runtime as a parent image
FROM python:3.8.0-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

# docker run -p 5000:5000 -d flask-app
# note logs for external served address for test

