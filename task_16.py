# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

import random
n = int(input("Введите число N-чисел массива: "))
my_massive = [random.randint(1, n) for i in range(n)] # пробую более короткий способ заполнения
# my_massive = []
# for i in range(n):
#     my_massive.append(random.randint(1, n))
print(my_massive)
count_x = 0
x = int(input("Введите число, частоту которого хотите найти в заданном массиве: "))
for i in range(len(my_massive)):
    if my_massive[i] == x:
        count_x += 1
print(count_x, "раз")