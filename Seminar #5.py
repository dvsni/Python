# ============================= Задача №1 =============================
# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтоюы выполнялось условие A[i] - 1 = A[i - 1]. Найдите это число.

# with open(r'E:\Разработчик\Знакомство с языком Python\Семинары\Seminar\seminar5.txt', 'w') as f:
#     f.write('1 2 3 \n4 5 6 8 \n9 10 \n')
#     f.write('77 78 \n79 80 81 \n')

# path = r'E:\Разработчик\Знакомство с языком Python\Семинары\Seminar\seminar5.txt'
# data = open(path, 'r')
# num_row = []
# for line in data:
#     print(line)
#     num_row += list(map(int, line.split()))
# data.close()
# print(num_row)

# for i, elem in enumerate(num_row[:-1]):
#     if elem + 1 != num_row[i + 1]:
#         print(elem + 1)
#         break

# ============================= Задача №2 =============================
# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность.
# *Пример*:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2 ,3] или [1, 6, 7] и т.д.

# num_list = [1, 5, 2, 3 , 4, 6, 1, 7]
# print(num_list, end=' =>')

# min_num = num_list[0]
# for i in range(len(num_list)):
#     order_list = []
#     order_list.append(num_list[i])
#     min_num = num_list[i]
#     for j in range(i, len(num_list) - 1):
#         if num_list[j] > min_num:
#             min_num = num_list[j]
#             order_list.append(num_list[j])
#         if len(order_list) > 1:
#             print(order_list, end=' ')


