from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


# Этот хэндлер срабатывает на команду /shop
@router.message(Command(commands=['shop']))
async def process_shop_command(message: Message):
    await message.answer(text=LEXICON_RU['/shop'])
