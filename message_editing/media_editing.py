from aiogram import Bot, Dispatcher, F
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAIU5WPJSt9TUFzUwbCqewIUNtp9gJBYAAIJxTEbp5JJSvDAdS74pTGAAQADAgADcwADLQQ',
    'photo_id2': 'AgACAgIAAxkBAAIU_WPJgB1KZiyEIu4OikbsEsJInzV-AALxxTEbp5JJSnu2IKkQdDDQAQADAgADcwADLQQ',
    'voice_id1': 'AwACAgIAAxkBAAIU52PJSwWbxtBrhoL8o3njUdvNaHckAALZJwACp5JJStGYVdp4u5cILQQ',
    'voice_id2': 'AwACAgIAAxkBAAIU9mPJfLxFoKpSTie3CZFL3PcFfTHhAAKWKQACp5JJSqoWOXKpDRntLQQ',
    'audio_id1': 'CQACAgIAAxkBAAIVRWPKsPl83xynqlF9YvF5MRyF9GxeAAL1JAACkhBZSmyFCDY61yX8LQQ',
    'audio_id2': 'CQACAgIAAxkBAAIVR2PKsXppkdhAnOlqwpOHDJivtfvJAAL4JAACkhBZSoMVyPSB59h5LQQ',
    'document_id1': 'BQACAgIAAxkBAAIVEmPKY_5RcBfEMeQ55X02PNimd1FdAAJ1IwACkhBRSmszrVZWfOY6LQQ',
    'document_id2': 'BQACAgIAAxkBAAIVFGPKZCYnp07PHr_OwXIKo5Z8fxcEAAJ3IwACkhBRSoZiZmUOrb4nLQQ',
    'video_id1': 'BAACAgIAAxkBAAIVFmPKZL_cgfokLm3pBU5w3zspn3-lAAJ5IwACkhBRSs4Lk37jVF8xLQQ',
    'video_id2': 'BAACAgIAAxkBAAIVGGPKZTURYRphKtnnVFHy8Oa6OxPXAAJ6IwACkhBRSnfUGQW2UKeBLQQ',
    }


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
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
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'photo')
    await message.answer_photo(
                        photo=LEXICON['photo_id1'],
                        caption='Это фото 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(F.data.in_(['text',
                               'audio',
                               'video',
                               'document',
                               'photo',
                               'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'photo')
    try:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=LEXICON['photo_id2'],
                                    caption='Это фото 2'),
                            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=LEXICON['photo_id1'],
                                    caption='Это фото 1'),
                            reply_markup=markup)


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.answer(
            text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)
