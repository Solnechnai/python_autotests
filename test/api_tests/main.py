import requests
import pytest

token = "0c433c5ee3cd92367729a5c068a118a2"
url = "https://api.pokemonbattle.ru/v2/"
HEADER = {"Content-Type" : "application/json", "trainer_token" : token}

# создание покемона
def test_create_pokemon():

    response_add_pokemon = requests.post (f"{url}pokemons", headers = HEADER, json= {
    "name": "Pokemm",
    "photo_id": -1
})
    assert response_add_pokemon.status_code == 201
    print(f'Статус код: {response_add_pokemon.status_code}. Сообщение: {response_add_pokemon.json()["message"]}')

# переименование покемона? смена картинки
def test_rename_pokemon():
    response_add_pokemon = requests.post(f"{url}pokemons", headers=HEADER, json={
        "name": "newpokemon",
        "photo_id": -1
    })
    pokemon_id = response_add_pokemon.json()["id"]

    response_rename_pokemon = requests.put (f"{url}pokemons", headers = {"trainer_token": token}, json= {
    "pokemon_id": pokemon_id,
    "name": "renamepokemon",
    "photo_id": 2
})
    print(f'Статус код: {response_rename_pokemon.status_code}. Сообщение: {response_rename_pokemon.json()["message"]}')

# ловля покемона
def test_get_pokemon(token_poc="0c433c5ee3cd92367729a5c068a118a2"):
    response_catch_pokemon = requests.post (f"{url}trainers/add_pokeball", headers = {"trainer_token": token_poc}, json= {
    "pokemon_id": "137926",
})
    print(f'Статус код: {response_catch_pokemon.status_code}. Сообщение: {response_catch_pokemon.json()["message"]}')