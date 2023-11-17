import time
import logging
import requests
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def normal_thread():
    logging.info('Thread normal')
    time.sleep(2)
    logging.info('El programa finaliza cuando este thread termina')


def daemon_thread():
    while True:
        logging.info('Daemon corriendo en segundo plano')
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target=daemon_thread, daemon=True)
    thread.start()
    
    input('Presiona una tecla para finalizar el thread principal\n')