# Напишите программу, которая будет на вход принимать число N и выводить число от -N до N

a = int(input())
# print(*range(-a, a+1)) - это вместо for
for i in range(-a, a+1):
    print(i, end=' ')
    