import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


jokes: dict[int, str] = {
    1: 'с хабра, описание фильмов Матрица\n\nСудя по всему, в городе машин либо очень либеральный мэр, либо очень криворукие сисадмины. Иначе как объяснить, что свободные люди беспрепятственно подключаются к вражеской ИТ-системе? Причем удаленно из тарантаса, летающего по канализации! Т.е. мало того, что у машин в сточных трубах развернут высокоскоростной Wi-Fi, так они еще и пускают в свою сеть всех подряд, позволяя неавторизованным пользователям получать данные из системы, вносить в нее изменения и общаться между собой. Красота!',
    2: '- У меня на одном курсе был фин, он приехал к нам т.к. был очарован культурой гопников. Он хотел проникнуться ею у первоисточника и подтянуть мат. И вот где-то в Питере он припал к истокам, все-все выучил и загорелся желанием принести культуру другим иностранцам группы. А там были бразильцы, немцы итальянцы, французы и китаец. И вот захожу как-то я в группу и там хором повторяют слова "ъуъ" и "съка" с шестью разными акцентами.\n- Хотелось бы послушать, как они говорили "ъуъ"',
    3: 'Я в восторге от наших учителей.\nСыну в школе дали домашнее задание, где, среди прочего, был вопрос "как связаны буква А4 и бык?"\nРассказал ему про финикийский алфавит, как первую фонетическую письменность. Что там была буква "алеф", очень похожая на нашу современную "А", и что слово "алеф" означало "бык". Что, возможно, букву так назвали, потому что если развернуть ее, то она похожа на морду быка с рогами.\nЕще очень радовался, что детям во втором классе такие вещи рассказывают.\nУчительница поставила ребенку двойку, заявив, что он фантазировал в домашнем задании. А правильный ответ: если к слову "бык" добавить "а", получится родительный падеж.\nЯ не планировал в таком раннем возрасте рассказывать сыну, что половина окружающих людей - идиоты, но, видимо, придется :-)',
    4: 'у меня на балконе сосулька растет метровая, прямо над машиной, которая ссигналит каждую ночь. Я эту сосульку из распылителя подкармливаю.',
    5: 'xx: Мне сейчас спам пришел "Я живу в доме напротив, вот моя ссылка *адрес ссылки*. Давай познакомимся". Я ответил, что живу напротив морга и меня пугают такие знакомства',
    6: 'xxx: В командировке на съемной квартире нужна была марля, чтобы погладить футболку. Начал шариться по всем ящикам. Марлю не нашел, зато нашел ключ в шкафу между простынями. Вспомнил, что один ящик в этом шкафу был заперт. Попробовал открыть его найденным ключом. Открыл. Внутри нашел марлю. Не зря в квесты играл..'
}


# Функция, генерирующая случайное число в диапазоне от 1 до длины словаря jokes
def random_joke() -> int:
    return random.randint(1, len(jokes))


# Этот хэндлер будет срабатывать на команды "/start" и "/joke"
@dp.message(Command(commands=['start', 'joke']))
async def process_start_command(message: Message):
    keyboard: list[list[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text='Хочу еще!', callback_data='more')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        text=jokes[random_joke()],
        reply_markup=markup
    )


# Этот хэндлер будет срабатывать на нажатие кнопки "Хочу еще!" и
# отправлять в чат новое сообщение, не удаляя старое
@dp.callback_query(F.data == 'more')
async def process_more_press(callback: CallbackQuery):
    keyboard: list[list[InlineKeyboardButton]] = [
        [InlineKeyboardButton(text='Хочу еще!', callback_data='more')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    # Отвечаем на callback, чтобы убрать часики
    await callback.answer()
    # Отправляем в чат новое сообщение с шуткой
    await callback.message.answer(
        text=jokes[random_joke()],
        reply_markup=markup
    )


# # Этот хэндлер будет срабатывать на нажатие кнопки "Хочу еще!" и
# # отправлять в чат новое сообщение с удалением старого
# @dp.callback_query(F.data == 'more')
# async def process_more_press(callback: CallbackQuery):
#     keyboard: list[list[InlineKeyboardButton]] = [
#         [InlineKeyboardButton(text='Хочу еще!', callback_data='more')]
#     ]
#     markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
#     # Удаляем сообщение, в котором была нажата кнопка
#     await callback.message.delete()
#     # Отправляем в чат новое сообщение с шуткой
#     await callback.message.answer(
#         text=jokes[random_joke()],
#         reply_markup=markup
#     )


# # Этот хэндлер будет срабатывать на нажатие кнопки "Хочу еще!"
# # и редактировать старое сообщение
# @dp.callback_query(F.data == 'more')
# async def process_more_press(callback: CallbackQuery):
#     keyboard: list[list[InlineKeyboardButton]] = [
#         [InlineKeyboardButton(text='Хочу еще!', callback_data='more')]
#     ]
#     markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
#     # Редактируем сообщение
#     await callback.message.edit_text(
#         text=jokes[random_joke()],
#         reply_markup=markup
#     )


# Этот хэндлер будет срабатывать на любые сообщения, кроме команд
@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text='Я даже представить себе не могу, '
             'что ты имеешь в виду :(\n\n'
             'Чтобы получить какую-нибудь шутку - '
             'отправь команду /joke'
    )


# Запускаем поллинг
if __name__ == '__main__':
    dp.run_polling(bot)
