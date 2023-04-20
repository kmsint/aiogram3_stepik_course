import asyncio
from datetime import datetime, timedelta

import tzlocal
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = 'BOT_TOKEN_HERE'


async def print_something_else(bot: Bot):
    print('something')
    await bot.send_message(chat_id=173901673, text='something')


async def main() -> None:
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    scheduler: AsyncIOScheduler = AsyncIOScheduler(
        timezone=str(tzlocal.get_localzone()))

    print(datetime.now())

    scheduler.add_job(print_something_else,
                      trigger='cron',
                      day_of_week='mon-sun',
                      hour=22,
                      minute=6,
                      args=(bot,))

    scheduler.add_job(print_something_else,
                      trigger='date',
                      run_date=datetime.now() + timedelta(seconds=5),
                      args=(bot,))

    scheduler.start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
