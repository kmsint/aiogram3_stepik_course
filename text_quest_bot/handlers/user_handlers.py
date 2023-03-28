import asyncio

from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message
from keyboards.kb_utils import create_inline_kb, create_reply_kb
from lexicon.lexicon import LEXICON
from states.states import FSMStartQuest

user_router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@user_router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(LEXICON['/start'])


# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@user_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@user_router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON['/cancel'])
    # Сбрасываем состояние
    await state.clear()


# Этот хэндлер будет срабатывать на команду "/beginning"
# и начинать квест, переводя игрока в состояние
@user_router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message, state: FSMContext):
    await message.answer(LEXICON['/beginning'])
    await asyncio.sleep(3)
    for i in range(1, 6):
        await message.answer(LEXICON[f'beginning_{i}'])
        await asyncio.sleep(4)
    reply_kb = create_reply_kb(1, 'yes_ready', 'maybe_ready', 'no_ready')
    await message.answer(text=LEXICON['beginning_6'],
                         reply_markup=reply_kb)
    await state.set_state(FSMStartQuest.ready_state)


# Этот хэндлер будет срабатывать на готовность игрока выполнить миссию
@user_router.message(Text(text=[LEXICON['yes_ready'],
                                LEXICON['maybe_ready']]),
                     StateFilter(FSMStartQuest.ready_state))
async def process_ready_answer(message: Message, state: FSMContext):
    if message.text == LEXICON['yes_ready']:
        await message.answer(LEXICON['yes_ready_answer'])
    else:
        await message.answer(LEXICON['maybe_ready_answer'])
    await asyncio.sleep(2)
    for i in range(1, 5):
        await message.answer(LEXICON[f'quest_started_{i}'])
        await asyncio.sleep(4)
    inline_kb = create_inline_kb(1, 'look_around', 'see_backpack', 'get_out')
    await message.answer(text=LEXICON['start_state_available_actions'],
                         reply_markup=inline_kb)
    await state.set_state(FSMStartQuest.start_state)


# Этот хэндлер будет срабатывать на отказ игрока выполнить миссию
@user_router.message(Text(text=LEXICON['no_ready']),
                     StateFilter(FSMStartQuest.ready_state))
async def process_no_ready_answer(message: Message, state: FSMContext):
    await message.answer(LEXICON['no_ready_answer'])
    await asyncio.sleep(3)
    await message.answer(LEXICON['no_ready_answer_1'])
    await asyncio.sleep(3)
    await message.answer(LEXICON['quest_failed'])
    await state.clear()
