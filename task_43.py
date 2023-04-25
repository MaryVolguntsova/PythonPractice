# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# import random
# def create_items():
#     len_items = int(input("Введите длину массива: "))
#     items = [random.randint(0, 20) for i in range(int(len_items))]
#     return items
my_items = [1, 2, 3, 2, 3, 2]

def find_pairs(items):
    count = 0
    for i in set(items):
        count += items.count(i) // 2
    return count

print(find_pairs(my_items))