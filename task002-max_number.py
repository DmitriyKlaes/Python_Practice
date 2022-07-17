# Напишите программу, которая на вход принимает 5 чисел и находит максимально из них.

a = list(map(int, input().split()))
b = a[0]
for i in a:
    if b < i:
        b = i
print(b)
