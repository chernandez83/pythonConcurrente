import time
import logging
import threading

from concurrent.futures import Future


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def callback_future(future):
    logging.info('Callback que se ejecuta hasta que el Future tenga un valor')
    logging.info(f'El Future es: {future.result()}')


if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(
        lambda future: logging.info(f'Callback con una lambda: {future.result()}')
    )

    logging.info('Iniciando tarea compleja')
    time.sleep(2)
    logging.info('Tarea compleja terminada')

    logging.info('Asignando valor al Future')
    future.set_result('TareaTerminada')
    logging.info('El Future ya tiene un valor')
