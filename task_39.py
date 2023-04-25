# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

def nums_list(n):
    result_list = []
    for i in range(n):
        result_list.append(int(input("Введите элемент")))
    return result_list

# функция, которая создает список
def create_list():
    list_1 = input("Введите числа через пробел: ").split()
    for k in range(len(list_1)):
        list_1[k] = int(list_1[k])
    return list_1

# мое решение
first_massive = create_list()
second_massive = create_list()
def diff_my_list(first_massive, second_massive):
    for num in first_massive:
        if num in second_massive:
            first_massive.remove(num)
    return first_massive
print(diff_my_list(first_massive, second_massive))

# решение группы
list_a = create_list()
list_b = create_list()
def dif_list(list_a, list_b):
    list_c = []
    for i in list_a:
        if i not in list_b:
            list_c.append(i)
    return list_c
print(dif_list(list_a, list_b))