# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. 
# Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

num = int(input("Введите число N: "))

def uniq_list(num):
    i = 20
    result_list = [i for i in range(i, num + 1) if i <= num and i % 20 == 0 or i % 21 == 0]
    return result_list

res = uniq_list(num)
print(res)
