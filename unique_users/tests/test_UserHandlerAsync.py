import pytest
import requests
import json

BASE_URL = 'http://localhost:8080'

def test_post_users():
    payload = {'name': 'Jean', 'application': 'app of jean'}
    r = requests.post(BASE_URL + '/user', json=payload)
    assert r.status_code == 201

def test_post_users_with_timestamp():
    payload = {'name': 'Jean', 'application': 'myapp', 'date': '20160415T200000Z'}
    r = requests.post(BASE_URL + '/user', json=payload)
    assert r.status_code == 201

def test_get_unique_users_amount_by_application_and_month_when_one_expected():
    r = requests.get(BASE_URL + '/user/application/myapp/month/4')
    assert r.status_code == 200
    assert r.text == '1'
