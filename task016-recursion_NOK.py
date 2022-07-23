# Задайте два число. Напишите программу, которая найдет НОК (наименьшее общее кратное)
# этих двух чисел. Алгоритм Евклида


def my_func(a, b):
    if b // a == 1:
        return a
    while a > b:
        a = a - b
    return my_func(b, a)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b:
    a = b
print(my_func(a, b))

