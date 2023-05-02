# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

indexes = []
import random
num = 15 #произвольно
new_list = [random.randint(0, 10) for i in range(num)]
print(new_list)

for i in range(len(new_list)):
    if new_list[i] >= min_value and new_list[i] <= max_value:
        indexes.append(i)

print("Индексы элементов, удовлетворяющих условию:", indexes)