# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# убрала это решение, так как оно усложняет задачу в сравнении с последоватльным введением чисел

# first_massive = input("Введите числа первого множества через пробел: ")
# second_massive = input("Введите числа второго множества через пробел: ")
# first_massive = list(first_massive.split())
# for i in range(len(first_massive)): first_massive[i].replace(" ", "") #убираем лишние пробелы, если они есть, тк они помешают сделать сортирвоку возрастанием
# second_massive = list(second_massive.split())
# for i in range(len(second_massive)): second_massive[i].replace(" ", "")

n = int(input("Введите величину первого множества: "))
m = int(input("Введите величину второго множества: "))
first_massive = [int(input("Вводите числа первого множества: ")) for i in range(n)] 
second_massive = [int(input("Вводите числа второго множества: ")) for i in range(m)] 
both_numbers = list()
for num in first_massive:
    if num in second_massive:
        both_numbers.append(num)
print(sorted(set(both_numbers)))

