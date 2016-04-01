import pytest
import requests

BASE_URL = 'http://localhost:8080'

def test_get_users():
    r = requests.get(BASE_URL + '/user')
    assert r.status_code == 200
