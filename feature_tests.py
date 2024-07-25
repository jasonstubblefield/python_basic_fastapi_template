# feature tests
import requests

def test_add_positive_numbers():
    url = "http://127.0.0.1:8000/add"
    params = {'a': 1, 'b': 2}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_add_negative_numbers():
    url = "http://127.0.0.1:8000/add"
    params = {'a': -1, 'b': -1}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.json() == {"result": -2}

def test_add_zero():
    url = "http://127.0.0.1:8000/add"
    params = {'a': 0, 'b': 0}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.json() == {"result": 0}