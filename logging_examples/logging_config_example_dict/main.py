import logging.config

from logging_settings import logging_config
from module_1 import main

# Загружаем настройки логирования из словаря `logging_config`
logging.config.dictConfig(logging_config)

# Исполняем функцию `main` из модуля `module_1.py`
main()