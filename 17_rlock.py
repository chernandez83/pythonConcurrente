import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


BALANCE = 100

lock = threading.RLock() # El mismo thread puede adquirir el recurso n veces 

if __name__ == '__main__':
    lock.acquire()
    lock.acquire()
    
    BALANCE -= 10
    
    lock.release()
    lock.release()
    
    logging.info(f'El thread principal finaliza con balance {BALANCE}')