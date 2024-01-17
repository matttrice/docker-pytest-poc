FROM python:3.8

COPY . /test
WORKDIR /test

RUN pip install -r requirements.txt

CMD ["pytest", "ping-test.py", "-rAs"]

# Run with BASE_URL of external flask application:
# $ docker run -e BASE_URL='http://172.17.0.2:5000' ping-test