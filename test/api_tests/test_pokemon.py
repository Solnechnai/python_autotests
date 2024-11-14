import requests
import pytest
import unittest

Url = "https://api.pokemonbattle.ru/"

# проверка статус-кода запроса информации о тренере
def test_status_code():
    response = requests.get(f"{Url}trainers", params={"trainer_id": 8549})
    assert response.status_code == 200

# проверка имени и города тренера
@pytest.mark.parametrize('key, value', [('trainer_name', 'Solnechnai')])
def test_pats_of_body(key, value):
    response = requests.get(f"{Url}v2/trainers", headers={'trainer_token': '0c433c5ee3cd92367729a5c068a118a2'}, params={"trainer_id":8549, "page":0})

    assert response.json()["data"][0][key] == value