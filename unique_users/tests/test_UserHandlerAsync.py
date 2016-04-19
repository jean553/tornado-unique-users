import pytest
import requests
import json

BASE_URL = 'http://localhost:8080'

def test_post_users():
    payload = {'name': 'Jean', 'application': 'app of jean'}
    r = requests.post(BASE_URL + '/user', json=payload)
    assert r.status_code == 201
