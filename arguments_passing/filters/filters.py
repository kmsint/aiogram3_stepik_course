from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject


class MyTrueFilter(BaseFilter):

    async def __call__(self, event: TelegramObject, my_int_var, my_text_var) -> bool:
        print('Попали внутрь фильтра', my_int_var, my_text_var)
        return True