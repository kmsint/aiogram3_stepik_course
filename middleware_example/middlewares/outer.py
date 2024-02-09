import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from cachetools import TTLCache

logger = logging.getLogger(__name__)

CACHE = TTLCache(maxsize=10_000, ttl=5)


class FirstOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        # logger.debug(
        #     'Вошли в миддлварь %s, тип события %s',
        #     __class__.__name__,
        #     event.__class__.__name__
        # )

        user: User = data.get('event_from_user')

        logger.debug('В кэше сейчас %s', CACHE)
        logger.debug('Id юзера %s', user.id)

        if user.id in CACHE:
            return

        CACHE[user.id] = True

        return await handler(event, data)


class SecondOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


class ThirdOuterMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        logger.debug(
            'Вошли в миддлварь %s, тип события %s',
            __class__.__name__,
            event.__class__.__name__
        )

        result = await handler(event, data)

        logger.debug('Выходим из миддлвари  %s', __class__.__name__)

        return result


async def first_outer_middleware(
    handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
    event: TelegramObject,
    data: Dict[str, Any]
) -> Any:

    logger.debug('Вошли в миддлварь-функцию')

    return await handler(event, data)