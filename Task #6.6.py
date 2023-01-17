# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# 1 решение: 
list_num = input('Введите числа через пробел: ').split()
print(list_num)
list_num = list(map(int, list_num))
print(max(list_num), min(list_num))

# 2 решение: 
def find_min_max(list_num):
    min_num = int(list_num[0])
    max_num = int(list_num[0])
    for num in list_num:
        num = int(num)
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    return max_num, min_num

def main():
    list_num = input('Введите числа через пробел: ').split()
    print(*find_min_max(list_num))

if __name__ == "__main__":
    main()

# Улучшение кода:

def Max(list1):
    list2 = list(map(int, list1.split()))
    return list2

list1 = input('Введите числа через пробел: ')
result = Max(list1)
print(min(result), max(result))