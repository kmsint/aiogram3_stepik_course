import asyncio

from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from keyboards.kb_utils import create_inline_kb, create_reply_kb
from lexicon.lexicon import LEXICON
from states.states import FSMStartQuest, FSMEngineeringCompartment

T_2: int = 0
T_3: int = 0
T_4: int = 0

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
    await state.update_data(backpack=set())
    await message.answer(LEXICON['/beginning'])
    await asyncio.sleep(T_2)
    for i in range(1, 6):
        await message.answer(LEXICON[f'beginning_{i}'])
        await asyncio.sleep(T_4)
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
        await message.answer(LEXICON['yes_ready_answer'],
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(LEXICON['maybe_ready_answer'],
                             reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(T_2)
    for i in range(1, 5):
        await message.answer(LEXICON[f'quest_started_{i}'])
        await asyncio.sleep(T_4)
    reply_kb = create_reply_kb(
                        1, 'look_around',
                        'see_backpack',
                        'get_out_engine_compartment')
    await message.answer(text=LEXICON['start_state_available_actions'],
                         reply_markup=reply_kb)
    await state.set_state(FSMStartQuest.start_state)


# Этот хэндлер будет срабатывать на отправку сообщения "Осмотреться"
# в состоянии FSMStartQuest.start_state
@user_router.message(Text(text=LEXICON['look_around']),
                     StateFilter(FSMStartQuest.start_state))
async def process_look_around_eng_msg(message: Message):
    for i in range(1, 5):
        await message.answer(LEXICON[f'look_around_eng_answ_{i}'])
        await asyncio.sleep(T_4)
    reply_kb = create_reply_kb(1, 'see_backpack',
                               'get_out_engine_compartment')
    await message.answer(text=LEXICON['look_around_eng_answ_5'],
                         reply_markup=reply_kb)


# Этот хэндлер будет срабатывать на нажатие кнопки "Проверить рюкзак"
# в любом состоянии, кроме дефолтного
@user_router.message(Text(text=LEXICON['see_backpack']),
                     ~StateFilter(default_state))
async def process_see_backpack_press(message: Message,
                                     state: FSMContext):
    backpack = await state.get_data()
    if backpack['backpack']:
        backpack_items_kb = create_inline_kb(1, *backpack['backpack'])
        await message.answer(text=LEXICON['backpack_items'],
                             reply_markup=backpack_items_kb)
    else:
        reply_kb = create_reply_kb(1, 'look_around',
                                   'see_backpack',
                                   'get_out_engine_compartment')
        await message.answer(text=LEXICON['backpack_empty'],
                             reply_markup=reply_kb)


# Этот хэндлер будет срабатывать на отправку сообщения
# "Покинуть двигательный отсек" и переводить в состояние
# FSMEngineeringCompartment.first_state
@user_router.message(Text(text=LEXICON['get_out_engine_compartment']),
                     StateFilter(FSMStartQuest.start_state))
async def process_get_out_engine_comprtment_msg(message: Message,
                                                state: FSMContext):
    await state.set_state(FSMEngineeringCompartment.first_state)
    for i in range(1, 3):
        await message.answer(
                text=LEXICON[f'engineering_compartment_{i}'])
        await asyncio.sleep(T_3)
    reply_kb = create_reply_kb(1, 'look_around',
                               'see_backpack',
                               'return_to_engine_compartment')
    await message.answer(text=LEXICON['engineering_compartment_3'],
                         reply_markup=reply_kb)


# Этот хэндлер будет срабатывать на сообщение "Осмотреться"
# в состоянии FSMStartQuest.start_state
@user_router.message(Text(text=LEXICON['look_around']),
                     StateFilter(FSMEngineeringCompartment.first_state))
async def process_look_around_engineerig_msg(message: Message):
    for i in range(1, 5):
        await message.answer(
                text=LEXICON[f'look_around_engineering_answ_{i}'])
        await asyncio.sleep(T_4)
    reply_kb = create_reply_kb(2, 'see_backpack',
                               'return_to_engine_compartment',
                               'go_to_med_compartment',
                               'go_to_bridge',
                               'take_spare_parts',
                               'take_tools')
    await message.answer(
                    text=LEXICON['look_around_engineering_answ_5'],
                    reply_markup=reply_kb)


# Этот хэндлер будет срабатывать на отказ игрока выполнить миссию
@user_router.message(Text(text=LEXICON['no_ready']),
                     StateFilter(FSMStartQuest.ready_state))
async def process_no_ready_answer(message: Message, state: FSMContext):
    await message.answer(LEXICON['no_ready_answer'],
                         reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(T_3)
    await message.answer(LEXICON['no_ready_answer_1'])
    await asyncio.sleep(T_3)
    await message.answer(LEXICON['quest_failed'])
    await state.clear()
