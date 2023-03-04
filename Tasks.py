# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств. Пример
# 11  6      2  4  6  8  10  12  10  8  6  4  2    3  6  9  12  15  18      6  12
# import random
# amount1 = int(input('Введите кол-во элементов 1 множества: '))
# amount2 = int(input('Введите кол-во элементов 2 множества: '))
# myList1 = [random.randint(1, 20) for _ in range(amount1)]
# myList2 = [random.randint(1, 20) for _ in range(amount2)]
# a = {element for element in myList1}
# b = {element for element in myList2}
# set = a.intersection(b)
# for i in myList1:
#     print(i, end=' ')
# print()
# for i in myList2:
#     print(i, end=' ')
# print()
# setNew = list(set)
# setNew.sort()
# for i in setNew:
#     print(i, end=' ')


