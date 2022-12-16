# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def f(n):
    result = []
    for i in range(1, n + 1):
        result.append((1+1/i)**i)
    return result
n = int(input('Введите целое число N: '))
print(f(n))
result = f(n)
def sum_list(result):
    sum = 0
    for i in range(len(result)):
        sum += result[i]
    return sum
print(f'Сумма = {sum_list(result)}')
