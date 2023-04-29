from typing import Iterator
from aiogram.filters.state import State, StatesGroup


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMShop(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    category = State()        # Состояние выбора категории товара
    subcategory = State()     # Состояние выбора подкатегории
    goods = State()           # Состояние выбора товара
    item = State()            # Состояние просмотра товара

    # Метод для получения предыдущего состояния из списка
    # состояний стейтгруппы
    @classmethod
    def get_previous_state(cls, state: State) -> State:
        states: Iterator[State] = iter(cls)
        result: State = next(states)

        for state_ in states:
            if state_ == state:
                break
            result = state_

        return result
