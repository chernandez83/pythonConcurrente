import time
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def fthread_1(event):
    logging.info('Thread 1')
    logging.info('Thread 1 - Esperando señal')
    
    event.wait()
    
    logging.info('Thread 1 - Señal recibida, bandera = True')
    

def fthread_2(event):
    logging.info('Thread 2')
    logging.info('Thread 2 - Enviando señal')
    
    time.sleep(2)
    event.set()
    
    logging.info('Thread 2 - Señal enviada')

def fthread_3(event):
    while not event.is_set():
        logging.info('Thread 3 - Esperando señal')
        time.sleep(0.5)


if __name__ == '__main__':
    
    event = threading.Event()
    
    thread_1 = threading.Thread(target=fthread_1, args=(event, ))
    thread_2 = threading.Thread(target=fthread_2, args=(event, ))
    thread_3 = threading.Thread(target=fthread_3, args=(event, ))
    
    thread_1.start()
    thread_2.start()
    thread_3.start()
    
    event.clear() # bandera = False