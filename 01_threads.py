import requests
import threading


def get_name():
    response = requests.get('https://randomuser.me/api/')
    
    print(response.status_code)
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
        

if __name__ == '__main__':
    # sequencial
    # for _ in range(1, 10):
    #     get_name()
        
    # concurrente
    for _ in range(1, 10):
        thread = threading.Thread(target=get_name)
        thread.start()