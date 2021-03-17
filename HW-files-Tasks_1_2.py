import os
file_path = os.path.join(os.getcwd(), 'recipes.txt')


def form_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            while True:
                dish_name = f.readline().strip()
                cook_book[dish_name] = []
                count_ing = int(f.readline().strip())
                for i in range(count_ing):
                  ing_list = f.readline().strip().split(' | ')
                  cook_book[dish_name].append({'ingredient': ing_list[0], 'quantity': int(ing_list[1]), 'measure': ing_list[2]})
                f.readline().strip()
        except ValueError:
            del cook_book['']
    return cook_book


print(form_cook_book('recipes.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    ing_dict = {}
    res = 0
    for j in dishes:
        for i in form_cook_book(file_path)[j]:
            if i['ingredient'] not in ing_dict:
                ing_dict[i['ingredient']] = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
            else:
                res = ing_dict[i['ingredient']]['quantity'] + i['quantity'] * person_count
                ing_dict[i['ingredient']] = ({'measure': i['measure'], 'quantity': res})
    return ing_dict


print()
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
