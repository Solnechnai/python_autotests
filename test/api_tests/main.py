import requests
import pytest

Token = "0c433c5ee3cd92367729a5c068a118a2"
Url = "https://pokemonbattle.ru/"

# регистрация тренера
def test_reg_trainer():

    response_trainer_reg = requests.post (f"{Url}trainers/reg", json= {
    "trainer_token": Token,
    "email": "gol8an@yandex.ru",
    "password": "Goon2024"
})
    print(response_trainer_reg.text)

# активация тренера
def test_activate_trainer():

    response_confirm_email = requests.post (f"{Url}trainers/confirm_email", json= {
    "trainer_token": Token
})
    print(response_confirm_email.text)

# создание покемона
def test_create_pokemone():

    response_add_pokemon = requests.post (f"{Url}pokemons", headers = {"trainer_token": Token}, json= {
    "name": "Пуля",
    "photo": "https://dolnikov.ru/pokemons/albums/027.png"
})
    print(response_add_pokemon.text)

# переименование покемона? смена картинки
def test_rename_pokemone():

    response_rename_pokemon = requests.put (f"{Url}pokemons", headers = {"trainer_token": Token}, json= {
    "pokemon_id": "126895",
    "name": "ariados",
    "photo": "https://dolnikov.ru/pokemons/albums/013.png"
})
    print(response_rename_pokemon.text)

# ловля покемона
def test_get_pokemone():
    response_catch_pokemon = requests.post (f"{Url}trainers/add_pokeball", headers = {"trainer_token": Token}, json= {
    "pokemon_id": "8855",
})
    print(response_catch_pokemon.text)