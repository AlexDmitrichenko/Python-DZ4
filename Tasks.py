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
# set1 = {element for element in myList1}
# set2 = {element for element in myList2}
# setNew = set1.intersection(set2)
# print(myList1)
# print(myList2)
# print(set1)
# print(set2)
# print(setNew)

