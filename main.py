import os
from pprint import pprint

def rest_menu(path):
    with open(path, encoding="utf-8") as file:
        menu = {}
        for cook in file:
            dish_name = cook[:-1]
            counter = file.readline().strip()
            list_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(["ingredient", "number", "measure"])
                ingridient = file.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items["ingredient"] = ingridient[0]
                    dish_items["number"] = ingridient[1]
                    dish_items["measure"] = ingridient[2]
                list_ingridient.append(dish_items)
                cook_book = {dish_name: list_ingridient}
                menu.update(cook_book)
            file.readline()

    return(menu)

rest_menu('Menu.txt')

def get_shop_list_by_dishes(dishes, persons=int):
    menu = rest_menu('Menu.txt')
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items = dict([(item["ingredient"], {'measure': item['measure'], "number": int(item["number"])*persons})])
                if shopping_list.get(item["ingredient"]):
                    extra_item = (int(shopping_list[item["ingredient"]]["number"]) +
                                  int(items[item["ingredient"]]["number"]))
                    shopping_list[item["ingredient"]]["number"] = extra_item

                else:
                    shopping_list.update(items)

        print(f"Необходимое количество ингридиентов для заказа {persons} клиентов")
        pprint(shopping_list)
    except KeyError:
        print("Не известное блюдо, повторите")


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

