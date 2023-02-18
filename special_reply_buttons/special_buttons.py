from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import (KeyboardButton, KeyboardButtonPollType, Message,
                           ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = 'BOT TOKEN HERE'

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(
                                text='Отправить телефон',
                                request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(
                                text='Отправить геолокацию',
                                request_location=True)
poll_btn: KeyboardButton = KeyboardButton(
                                text='Создать опрос/викторину',
                                request_poll=KeyboardButtonPollType())


# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
                                    resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=keyboard)

# Создаем кнопки
poll_btn_2: KeyboardButton = KeyboardButton(
                                text='Создать опрос',
                                request_poll=KeyboardButtonPollType(
                                                        type='regular'))

quiz_btn: KeyboardButton = KeyboardButton(
                                text='Создать викторину',
                                request_poll=KeyboardButtonPollType(
                                                        type='quiz'))

# Инициализируем билдер
poll_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер
poll_kb_builder.row(poll_btn_2, quiz_btn, width=1)

# Создаем объект клавиатуры
poll_keyboard: ReplyKeyboardMarkup = poll_kb_builder.as_markup(
                                        resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/poll"
@dp.message(Command(commands='poll'))
async def process_poll_command(message: Message):
    await message.answer(text='Экспериментируем с кнопками опрос/викторина',
                         reply_markup=poll_keyboard)


# Создаем кнопку
web_app_btn: KeyboardButton = KeyboardButton(
                                text='Start Web App',
                                web_app=WebAppInfo(url="https://stepik.org/"))

# Создаем объект клавиатуры
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                            text='Start Web App',
                                            keyboard=[[web_app_btn]],
                                            resize_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/web_app"
@dp.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=web_app_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
