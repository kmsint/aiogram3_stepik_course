from database import CATEGORIES, SUBCATEGORIES, GOODS


class Goods:
    def __init__(self, goods_id: int) -> None:
        self._goods_id = goods_id
        self._goods = GOODS[goods_id]
        self._goods_name = self._get_goods_name()
        self._subcategory_name = self._get_subcategory_name()
        self._price = self._get_price()

    def _get_subcategory_name(self):
        return SUBCATEGORIES[GOODS[self._goods_id][1]][0]

    def _get_price(self):
        return GOODS[self._goods_id]

    def _get_


def get_categories():
    return list(CATEGORIES.items())


def get_subcategories(category: int) -> list[tuple]:
    subcategories_list: list = []
    for item in SUBCATEGORIES.items():
        if item[1][1] == category:
            subcategories_list.append(item)
    return subcategories_list


def get_goods(subcategory: int) -> list[tuple]:
    goods_list: list = []
    for item in GOODS.items():
        if item[1][1] == subcategory:
            goods_list.append(item)
    return goods_list


print(get_categories())
print(get_subcategories(2))
print(get_goods(2))

goods_1 = Goods(4)
print(goods_1.get_subcategory_name())
