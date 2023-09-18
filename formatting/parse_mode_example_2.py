from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет!\n\nЯ бот, демонстрирующий '
             'как работает HTML-разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/bold - жирный текст\n'
             '/italic - наклонный текст\n'
             '/underline - подчеркнутый текст\n'
             '/spoiler - спойлер'
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='Я бот, демонстрирующий '
             'как работает HTML-разметка. Отправь команду '
             'из списка ниже:\n\n'
             '/bold - жирный текст\n'
             '/italic - наклонный текст\n'
             '/underline - подчеркнутый текст\n'
             '/spoiler - спойлер'
    )


# Этот хэндлер будет срабатывать на команду "/bold"
@dp.message(Command(commands='bold'))
async def process_bold_command(message: Message):
    await message.answer(
        text='<b>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'делающая текст жирным.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</b>'
    )


# Этот хэндлер будет срабатывать на команду "/italic"
@dp.message(Command(commands='italic'))
async def process_italic_command(message: Message):
    await message.answer(
        text='<i>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'делающая текст наклонным.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</i>'
    )


# Этот хэндлер будет срабатывать на команду "/underline"
@dp.message(Command(commands='underline'))
async def process_underline_command(message: Message):
    await message.answer(
        text='<u>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'делающая текст подчеркнутым.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</u>'
    )


# Этот хэндлер будет срабатывать на команду "/spoiler"
@dp.message(Command(commands='spoiler'))
async def process_spoiler_command(message: Message):
    await message.answer(
        text='<tg-spoiler>Это текст, демонстрирующий '
             'как работает HTML-разметка, '
             'убирающая текст под спойлер.\n\n'
             'Чтобы еще раз посмотреть список доступных команд - '
             'отправь команду /help</tg-spoiler>'
    )


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд,
# отлавливаемых хэндлерами выше
@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду\n\n'
             'Чтобы посмотреть список доступных команд - '
             'отправь команду /help'
    )


# Запускаем поллинг
if __name__ == '__main__':
    dp.run_polling(bot)
