import logging

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)


# Определяем свой фильтр, наследуюясь от класса `Filter` библиотеки `logging`
class CriticalLogFilter(logging.Filter):
    # Переопределяем метод `filter`, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname == 'CRITICAL'


# Инициализируем форматтер
formatter_3 = logging.Formatter(
    fmt='#%(levelname)-8s [%(asctime)s] - %(message)s'
)

# Инициализируем первый хэндлер, который будет писать логи в `stderr`
stderr = logging.StreamHandler()
# Инициализируем второй хэндлер, который будет писать логи в файл `critical_logs.txt`
critical_file = logging.FileHandler('critical.log', mode='w')

# Определяем форматирование логов во втором хэндлере
critical_file.setFormatter(fmt=formatter_3)

# Добавляем второму хэндлеру фильтр `CriticalLogFilter`, который будет
# пропускать в хэндлер только логи уровня `CRITICAL`
critical_file.addFilter(CriticalLogFilter())

# Добавляем хэндлеры к логгеру
logger.addHandler(stderr)
logger.addHandler(critical_file)


def square_number(number: int | float):

    logger.critical('Вошли в функцию %s', square_number.__name__)

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    logger.critical('Вышли из функции %s', square_number.__name__)

    return number**2