import time
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


class ClaseThread(threading.Thread):
    def __init__(self, name, daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)
    
    
    def run(self):
        logging.info('Tareas que se ejecutan de forma concurrente')
        if self.daemon:
            while True:
                logging.info('Ejecutando demonio')

if __name__ == '__main__':
    thread = ClaseThread('ClaseThread', True)
    thread.start()
    
    time.sleep(0.05)
    logging.info('Fin del programa')