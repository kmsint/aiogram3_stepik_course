import logging

from module_1 import main

# Настраиваем базовую конфигурацию логирования
logging.basicConfig(
    format='#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
)

logger = logging.getLogger(__name__)

handler_main = logging.StreamHandler()
logger.addHandler(handler_main)

# Исполняем функцию `main` из модуля `module_1.py`
main()