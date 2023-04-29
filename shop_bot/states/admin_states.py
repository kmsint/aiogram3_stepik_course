from aiogram.filters.state import State, StatesGroup


# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMAddingSKU(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    category_selection = State()        # Состояние выбора категории товара
    subcategory_selection = State()     # Состояние выбора подкатегории
    item_name = State()                 # Состояние заполнения названия товара
    item_price = State()                # Состояние заполнения цены товара
    item_description = State()          # Состояние заполнения описания товара
    item_size = State()                 # Состояние заполнения размера товара
    item_quantity = State()             # Состояние заполнения количества товара
    item_photo = State()                # Состояние отправки фото товара
