from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаем список списков с кнопками
keyboard: list[KeyboardButton] = [
    KeyboardButton(text=str(i)) for i in range(1, 8)]

# Инициализируем билдер
builder = ReplyKeyboardBuilder()

builder.row(*keyboard, width=3)

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем с обычными кнопками',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
