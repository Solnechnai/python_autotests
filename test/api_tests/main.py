import requests
import pytest

token = "0c433c5ee3cd92367729a5c068a118a2"
url = "https://api.pokemonbattle.ru/v2/"
HEADER = {"Content-Type" : "application/json", "trainer_token" : token}

# создание покемона

response_add_new_pokemon = requests.post (f"{url}pokemons", headers = HEADER, json= {
    "name": "Pokemm",
    "photo_id": -1
})

print(response_add_new_pokemon.json())

#pokemon_id = response_add_new_pokemon.json()["id"]

print(f'Статус код: {response_add_new_pokemon.status_code}. Сообщение: {response_add_new_pokemon.json()["message"]}')

# переименование покемона? смена картинки
response_add_pokemon = requests.post(f"{url}pokemons", headers=HEADER, json={
        "name": "newpokemon",
        "photo_id": -1
    })

response_rename_pokemon = requests.put (f"{url}pokemons", headers = {"trainer_token": token}, json= {
    "pokemon_id": "142827",
    "name": "renamepokemon",
    "photo_id": 2
})
print(f'Статус код: {response_rename_pokemon.status_code}. Сообщение: {response_rename_pokemon.json()["message"]}')

# ловля покемона
response_catch_pokemon = requests.post (f"{url}trainers/add_pokeball", headers = {"trainer_token": token}, json= {
    "pokemon_id": "142827",
})
print(f'Статус код: {response_catch_pokemon.status_code}. Сообщение: {response_catch_pokemon.json()["message"]}')