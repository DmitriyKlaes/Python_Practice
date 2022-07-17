# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов, заполненных случайными числами.

a = int(input())
b = 1
for i in range(a):
    print(b, end=' ')
    b = b * (-3)
    


from random import randint
print(randint(1, 10))