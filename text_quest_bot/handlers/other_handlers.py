from aiogram import Router
from aiogram.types import Message

other_router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@other_router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')
