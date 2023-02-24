from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message,
                           ReplyKeyboardMarkup)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = 'BOT TOKEN HERE'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

keyboard: list[list[KeyboardButton]] = [[KeyboardButton(
    text=f'Кнопка {j * 3 + i}') for i in range(1, 4)] for j in range(3)]

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем с обычными кнопками',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
