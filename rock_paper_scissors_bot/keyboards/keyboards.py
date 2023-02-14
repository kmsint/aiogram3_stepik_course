from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU


button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_yes],
                                              [button_no]],
                                    one_time_keyboard=True,
                                    resize_keyboard=True)




button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])


# Создаем игровую клавиатуру с кнопками "Камень 🗿", "Ножницы ✂" и "Бумага 📜"
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1],
                                              [button_2],
                                              [button_3]],
                                    resize_keyboard=True)
