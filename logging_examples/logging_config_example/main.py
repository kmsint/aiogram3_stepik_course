import logging

from module_1 import main

# Настраиваем базовую конфигурацию логирования
logging.basicConfig(
    format='#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
)

# Исполняем функцию `main` из модуля `module_1.py`
main()