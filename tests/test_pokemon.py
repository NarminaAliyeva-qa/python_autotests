"""
Вывод всех покемонов

"""
# import requests
# import pytest

URL = 'https://api.pokemonbattle.me:9104'

HEADER = {
    'Content-Type': 'application/json',
}

# def test_get_trainers():
#     response = requests.get(url=f'{URL}/trainers')
#     assert response.status_code == 200, 'unexpected status'
    
#     Выводим статус код и текст ответа
#     print(response.status_code)
#     print(response.text)

"""
Тест с id покемона

"""

import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'

HEADER = {
    'Content-Type': 'application/json',
}

def test_get_trainers():
    PARAMS = {'trainer_id': 4751}  # параметры запроса
    response = requests.get(url=f'{URL}/trainers', params=PARAMS)
    assert response.status_code == 200, f'unexpected status: {response.status_code}'
    
    # Выводим статус код и текст ответа
    print(response.status_code)
    print(response.text)