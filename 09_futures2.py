import logging
import requests
import threading
from concurrent.futures import Future


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def generate_request(url):
    future = Future()
    
    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread.start()
    
    return future


def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')
        
        logging.info(f'Pokemon: {name}')


if __name__ == '__main__':
    future = generate_request('https://pokeapi.co/api/v2/pokemon/1/')
    future.add_done_callback(
        lambda future: show_pokemon_name(future.result())
    )
    
    while not future.done():
        logging.info('Esperando resultado')
    else:
        logging.info('Programa terminado')