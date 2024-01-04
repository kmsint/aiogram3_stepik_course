import logging

from module_2 import devide_number
from module_3 import square_number

logger = logging.getLogger(__name__)


def main():
    a, b = 12, 2
    c, d = 4, 0

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    print(devide_number(a, square_number(b)))
    print(devide_number(square_number(c), d))