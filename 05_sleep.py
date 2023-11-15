import time
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def task():
    logging.info('Ejecutando nueva tarea')
    time.sleep(2)
    logging.info('Tarea finalizada')


if __name__ == '__main__':
    thread = threading.Thread(target=task)
    thread.start()
    
    contador = 0
    while True:
        time.sleep(1)
        contador += 1
        logging.info(f'Tiempo transcurrido: {contador} segundos')
        if contador > 3:
            break