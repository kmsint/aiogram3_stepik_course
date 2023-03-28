import asyncio
import requests

from aiogram import Bot, Dispatcher
from aiogram.types import InputFile, URLInputFile, Message, ChatMemberLeft, ContentType
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.filters import CommandStart

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# API_TOKEN: str = 'BOT TOKEN HERE'
API_TOKEN: str = '5424991242:AAFbT6ckF2HYKPDyLWLFvx5C2jV71TsG9vQ'
# Создаем объекты бота и диспетчера

scheduler: AsyncIOScheduler = AsyncIOScheduler(timezone='Europe/Moscow')

b = int()


async def cat_photo_every_day(bot: Bot):
    # cat_photo = URLInputFile(requests.get('https://aws.random.cat/meow').json()['file'])
    await bot.send_message(chat_id=173901673, text='Какой-то текст')
    # await bot.send_photo(chat_id=173901673, photo=cat_photo)



async def main():
    bot: Bot = Bot(token=API_TOKEN)
    dp: Dispatcher = Dispatcher()

    scheduler.add_job(cat_photo_every_day,
                      trigger='cron',
                      hour='00',
                      minute='45',
                      args=(bot, ))

    scheduler.start()

    # dp.message.register(cat_photo_every_day, CommandStart())
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
