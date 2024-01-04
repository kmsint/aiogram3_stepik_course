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
formatter = logging.Formatter(
    fmt='#%(levelname)-8s [%(asctime)s] - %(message)s'
)

# Инициализируем первый хэндлер, который будет писать логи в `stderr`
handler_1 = logging.StreamHandler()
# Инициализируем второй хэндлер, который будет писать логи в файл `critical_logs.txt`
handler_2 = logging.FileHandler('critical.log', mode='w')

# Определяем форматирование логов во втором хэндлере
handler_2.setFormatter(fmt=formatter)

# Добавляем второму хэндлеру фильтр `CriticalLogFilter`, который будет
# пропускать в хэндлер только логи уровня `CRITICAL`
handler_2.addFilter(CriticalLogFilter())

# Добавляем хэндлеры в логгер
logger.addHandler(handler_1)
logger.addHandler(handler_2)


def square_number(number: int | float):

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    return number**2