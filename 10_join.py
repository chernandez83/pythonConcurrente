import time
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def conexion_bd():
    logging.info('Conectando a bd')
    time.sleep(2)


def consulta_servidor_web():
    logging.info('Consulta al servidor')
    time.sleep(2)


if __name__ == '__main__':
    thread1 = threading.Thread(target=conexion_bd)
    thread2 = threading.Thread(target=consulta_servidor_web)
    
    thread1.start()
    thread2.start()
    
    # Esperar a que terminen los threads
    thread1.join()
    thread2.join()
    
    logging.info('Fin del programa, los threads han finalizado')