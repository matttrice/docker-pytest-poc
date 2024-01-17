import requests
import os


def test_ping():
    BASE_URL = (
        os.environ["BASE_URL"] if "BASE_URL" in os.environ else "http://localhost:5000"
    )
    print(f"BASE_URL={BASE_URL}")

    url = f"{BASE_URL}/ping/"
    param = "horsetooth"
    response = requests.get(url + param)
    print(response.content)
    assert response.status_code == 200
    assert response.content == param.encode("utf-8")
