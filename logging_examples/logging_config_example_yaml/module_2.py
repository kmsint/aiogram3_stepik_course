import logging

logger = logging.getLogger(__name__)


def devide_number(dividend: int | float, devider: int | float):

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')