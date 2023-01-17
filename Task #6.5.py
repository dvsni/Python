# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# my_list = ["123", "234", 123, '567']
# print(my_list)

# string_find = "123"
# count = 0
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count += 1
#         if count == 2:
#             print(i)
# else:
#     print(-1)

my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_str = input('Введите строку')

if my_list.count(my_str) > 1:
    first_index = my_list.index(my_str)
    print(my_list.index(my_str, first_index + 1))
else:
    print(-1)

# Улучшение кода:

from typing import List 

def find_second_entry(str_list: List[str], search_word: str):
    try:
        return [i for i, elem in enumerate(str_list) if elem == search_word][1]
    except IndexError:
        return -1