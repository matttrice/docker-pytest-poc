import requests


def test_ping():
    url = "http://localhost:5000/ping/"
    param = "horsetooth"
    response = requests.get(url + param)
    print(response.content)
    assert response.status_code == 200
    assert response.content == param.encode("utf-8")
