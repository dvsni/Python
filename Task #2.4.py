# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

with open('List.txt','r') as f:
    a = f.read().split('\n')
a = list(map(int, a))
n = int(input('Введите число: '))
gen = [i for i in range(-n, n+1)]
kn = 1
for i in a:
    kn *= gen[i]
    print(kn)
print(a)
print(gen)
print(kn)
