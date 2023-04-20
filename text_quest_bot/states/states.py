from aiogram.filters.state import State, StatesGroup


class FSMStartQuest(StatesGroup):
    ready_state = State()
    start_state = State()


class FSMEngineeringCompartment(StatesGroup):
    first_state = State()
