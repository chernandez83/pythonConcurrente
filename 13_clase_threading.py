import time
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def current_thread_info():
    current_thread = threading.current_thread()
    name = current_thread.name
    id = threading.get_ident()

    logging.info(f'Thread actual: {current_thread} - {name}')
    logging.info(f'ID: {id}')


def nueva_tarea():
    current_thread_info()


if __name__ == '__main__':
    thread1 = threading.Thread(target=nueva_tarea, name='thread-b')
    thread1.start()

    current_thread_info()
    
    logging.info(f'Threads activos: {threading.enumerate()}')
    
    for thread in threading.enumerate():
        if thread == threading.main_thread():
            logging.info('Thread principal')
        logging.info(thread)