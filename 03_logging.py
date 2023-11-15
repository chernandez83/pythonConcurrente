import logging
# Debug 10, Info 20, Warning 30, Error 40, Critical 50


# Cambinar nivel de logging # default: 30
logging.basicConfig(
    level=logging.DEBUG,
    #format='%(filename)s %(asctime)s %(message)s %(funcName)s %(levelname)s %(lineno)s %(module)s %(name)s %(pathname)s',
    format='%(message)s %(thread)s %(threadName)s %(process)s %(processName)s'
    #datefmt='%H:%M:%S',
    #filename='messages.txt'
) 


def mis_mensajes():
    logging.debug('Debug 10')
    logging.info('Info 20')
    logging.warning('Warning 30')
    logging.error('Error 40')
    logging.critical('Critical 50')


if __name__ == '__main__':
    mis_mensajes()