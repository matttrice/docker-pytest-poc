FROM python:3.8

COPY . /test
WORKDIR /test

RUN pip install -r requirements.txt

CMD ["pytest", "ping-test.py", "-rAs"]