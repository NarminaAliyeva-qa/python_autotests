"""
Создать покемона

"""

#import requests


URL = 'https://api.pokemonbattle.me:9104'

HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': '3fa81d8573bc7a419c65bf605ddd022a'
}

body = {
    "name": "Gexon",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

# response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)

# Выводим статус код и текст ответа
# print(response.status_code)
# print(response.text)

"""
Изменить имя покемона

"""


# import requests

URL = 'https://api.pokemonbattle.me:9104'


HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': '3fa81d8573bc7a419c65bf605ddd022a'
}

body = {
    "pokemon_id": "29707",
    "name": "Nunmu",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

# response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)

# Выводим статус код и текст ответа
# print(response.status_code)
# print(response.text)

"""
добавить в покебол

"""
import requests

URL = 'https://api.pokemonbattle.me:9104'


HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': '3fa81d8573bc7a419c65bf605ddd022a'
}

body = {
    "pokemon_id": "29703"
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)

# Выводим статус код и текст ответа
# print(response.status_code)
# print(response.text)