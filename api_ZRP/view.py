from os import getenv
import requests
from flask import jsonify


def catch_abilities(info: dict) -> dict:
    ablt = [ v3 for v1 in info for k2, v2 in v1.items() if type(v2) == dict for k3, v3 in v2.items() if k3 == 'name']
    ablt.sort()
    return {'abilities': ablt}


def catch_items(info: dict) -> list:
    return [ {'name':v2['name']} for v1 in info if type(v1) == dict for k2, v2 in v1.items() if type(v2) == dict ]


def atach_cost_to_item(info: dict, items: list) -> list:
    url_cost = [ v2['url'] for v1 in info if type(v1) == dict for k2, v2 in v1.items() if type(v2) == dict ]
    for idx, url in enumerate(url_cost):
        valor = requests.get(f'{url}')
        items[idx]['cost'] = valor.json()['cost']
    return items


def init_app(app):
    
    url_pokemon = getenv('URL_POKEMON') if getenv('URL_POKEMON').endswith('/') else getenv('URL_POKEMON') + '/'
    if not url_pokemon:
        url_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    
    @app.route('/')
    def index():
        return '''
            <h1>Sistema para verificar dados de Pokemons</h1><br>
            <h4>Use a URL http://localhost:8000/api/pokemons/<nome_do_pokemon> para testar o sistema</h4><br>
            Alguns exemplos de nomes de pokemons: ditto, snubbull, girafarig, miltank, sharpedo etc. 
        '''

    @app.route('/api/pokemons/<pokemon_name>')
    def pokemon_data(pokemon_name):
        pokemon = requests.get(f"{url_pokemon}{pokemon_name}")
        if pokemon:
            abilities = catch_abilities(pokemon.json()['abilities'])
            items = catch_items(pokemon.json()['held_items'])
            items_with_cost = atach_cost_to_item(pokemon.json()['held_items'], items)
            abilities.update({'items': items_with_cost})
            return jsonify(abilities)
        else:
            return jsonify('Nao encontrado. Verifique a URL passada.')
