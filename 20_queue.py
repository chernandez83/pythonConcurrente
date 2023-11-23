import time
import queue
import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s: %(message)s'
)


def show_elements(queue):
    while not queue.empty():
        item = queue.get()
        logging.info(f'Elemento: {item}')
        
        queue.task_done() # libera la cola para otros threads
        time.sleep(0.5)


if __name__ == '__main__':
    m_queue = queue.Queue()
    
    for val in range(1, 21):
        m_queue.put(val)
    
    logging.info('Elementos cargados en la cola')
    
    for _ in range(4):
        thread = threading.Thread(target=show_elements, args=(m_queue, ))
        thread.start()