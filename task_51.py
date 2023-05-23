# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

def same_by(characteristic, objects):
    # f1 = characteristic(objects[0])
    # [i for i in objects if i == x]
    res = list(map(lambda obj: characteristic(obj) == characteristic(objects[0]), objects))
    # return [characteristic(i) for i in objects if characteristic(i) == x]
    return all(res)
# если убрать all, то будет bool по каждому из элементов списка. Мы ставим all
# чтобы проверить, все эти элементы соотв условию, если нет, он делает вывод по всем

values = [0, 2, 10, 6, 8] 
print(same_by(lambda x: x % 2, values))

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')