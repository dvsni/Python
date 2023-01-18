# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

# 1 вариант:
from itertools import groupby

def thesaurus(*args):
    if "" not in args:
        return{ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))

# 2 вариант:
def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]
    return names_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))

