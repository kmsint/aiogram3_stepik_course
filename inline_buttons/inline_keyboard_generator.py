from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()

LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7',}

BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11'}


# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Добавляем в билдер последнюю кнопку, если она передана в функцию
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
                            text=last_btn,
                            callback_data='last_btn'))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(4, last_btn='Последняя кнопка', **BUTTONS)
    await message.answer(text='Это инлайн-клавиатура, сформированная функцией '
                              '<code>create_inline_kb</code>',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
