from typing import Optional

from aiogram.filters.callback_data import CallbackData


class MyCallbackFactory(CallbackData, prefix="any"):
    action: str
    value: Optional[int]
