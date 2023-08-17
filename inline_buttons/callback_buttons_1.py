from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = 'BOT TOKEN HERE'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты инлайн-кнопок
big_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed')

big_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed')

# Создаем объект инлайн-клавиатуры
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]])


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру с инлайн-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки. Нажми на любую!',
                         reply_markup=keyboard)


# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed' или 'big_button_2_pressed'
@dp.callback_query(F.data.in_(['big_button_1_pressed',
                               'big_button_2_pressed']))
async def process_buttons_press(callback: CallbackQuery):
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
