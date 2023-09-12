from aiogram import F, Router

from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


@router.message(F.sticker)
async def send_echo_sticker(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer_sticker(sticker=message.sticker.file_id)


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
