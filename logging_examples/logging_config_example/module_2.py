import logging
import sys

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

# Определяем свой фильтр, наследуюясь от класса Filter библиотеки logging
class DebugWarningLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING')

# Инициализируем форматтер
formatter_2 = logging.Formatter(
    fmt='#%(levelname)-8s [%(asctime)s] - %(filename)s:'
        '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
)

# Инициализируем хэндлер, который будет писать логи в `stdout`
stdout = logging.StreamHandler(sys.stdout)

# Добавляем хэндлеру фильтр `DebugWarningLogFilter`, который будет пропускать в
# хэндлер только логи уровня `DEBUG` и `WARNING`
stdout.addFilter(DebugWarningLogFilter())

# Определяем форматирование логов в хэндлере
stdout.setFormatter(formatter_2)

# Добавляем хэндлер к логгеру
logger.addHandler(stdout)


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