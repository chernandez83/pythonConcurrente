import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


# Timer
def callback():
    logging.info('Callback que no se ejecuta de forma inmediata')


if __name__ == '__main__':
    thread = threading.Timer(3, callback)
    thread.start()
    
    logging.info('Thread principal')
    logging.info('Esperando la ejecución del callback')