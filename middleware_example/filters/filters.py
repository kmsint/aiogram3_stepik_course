import logging

from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class MyTrueFilter(BaseFilter):

    async def __call__(self, event: TelegramObject) -> bool:
        logger.debug('Попали внутрь фильтра %s', __class__.__name__)
        return True


class MyFalseFilter(BaseFilter):

    async def __call__(self, event: TelegramObject) -> bool:
        logger.debug('Попали внутрь фильтра %s', __class__.__name__)
        return False