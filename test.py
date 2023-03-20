import logging

logging.basicConfig(filename='logger.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


def log():
    i = 0
    while i < 10:
        logging.error(i)
        i += 1


if __name__ == '__main__':
    log()
