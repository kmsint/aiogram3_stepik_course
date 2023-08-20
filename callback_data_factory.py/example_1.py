from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Создаем свой класс фабрики коллбэков, указывая префикс
# и структуру callback_data
class GoodsCallbackFactory(CallbackData, prefix="goods"):
    category_id: int
    subcategory_id: int
    item_id: int


# Создаем объекты кнопок, с применением фабрики коллбэков
button_1: InlineKeyboardButton = InlineKeyboardButton(
                    text='Категория 1',
                    callback_data=GoodsCallbackFactory(
                                            category_id=1,
                                            subcategory_id=0,
                                            item_id=0).pack())

button_2: InlineKeyboardButton = InlineKeyboardButton(
                    text='Категория 2',
                    callback_data=GoodsCallbackFactory(
                                            category_id=2,
                                            subcategory_id=0,
                                            item_id=0).pack())

# Создаем объект клавиатуры, добавляя в список списки с кнопками
markup: InlineKeyboardMarkup = InlineKeyboardMarkup(
                    inline_keyboard=[[button_1],
                                     [button_2]])


# Этот хэндлер будет срабатывать на команду /start
# и отправлять пользователю сообщение с клавиатурой
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая клавиатура',
                         reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие любой
# инлайн кнопки и распечатывать апдейт в терминал
@dp.callback_query()
async def process_any_inline_button_press(callback: CallbackQuery):
    print(callback.model_dump_json(indent=4, exclude_none=True))
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
