from aiogram import Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from filters.filters import MyTrueFilter
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart(), MyTrueFilter())
async def process_start_command(message: Message, some_dict, my_int_var, my_text_var):
    await message.answer(text=LEXICON_RU['/start'])
    await message.answer(text=some_dict[1])
    await message.answer(text=my_text_var)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message, data):
    await message.answer(text=str(data))
