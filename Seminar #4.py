# ============================= Задача №1 =============================
# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# 1 решение: 
# list_num = input('Введите числа через пробел: ').split()
# print(list_num)
# list_num = list(map(int, list_num))
# print(max(list_num), min(list_num))

# 2 решение: 
# def find_min_max(list_num):
#     min_num = int(list_num[0])
#     max_num = int(list_num[0])
#     for num in list_num:
#         num = int(num)
#         if max_num < num:
#             max_num = num
#         if min_num > num:
#             min_num = num
#     return max_num, min_num

# def main():
#     list_num = input('Введите числа через пробел: ').split()
#     print(*find_min_max(list_num))

# if __name__ == "__main__":
#     main()

# ============================= Задача №2 =============================
# Найдите корни квадратного уровнения Ax^2 + Bx + C двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# list_num = input("Введите значения коэффициентов a,b и z через пробел: ").split()
# print(list_num)

# a, b, z = list(map(int, list_num))
# d = b ** 2 - 4 * a * z
# if d < 0:
#     print("Корней нет")
# elif d == 0:
#     x = -b / (2 * a)
#     print(f'x_ = {x}', end=' ')
# else:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     print(f'x1_ = {x1}', end=' ')
#     x2 = (-b - d ** 0.5) / (2 * a)
#     print(f'x2_ = {x2}')

# ============================= Задача №3 =============================
# Задайте два числа. Напишите программу, которая найдет НОК
# (наименьшее общее кратное) этих двух чисел.

# a, b = int(input('Введите а: ')), int(input('Введите b: '))
# max_num = max(a, b)
# for i in range(max_num, (a * b) + 1, max_num):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break