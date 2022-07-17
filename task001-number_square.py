# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# print ('Введите первое число: ')
# number_one = int(input())
# print ('Введите второе число: ')
# number_two = int(input())

# if number_one * number_one == number_two:
#     print('Да')
# else:
#     print('Нет')

a,b = map(int, input().split())
if a ** 2 == b or b ** 2 == a:
    print('Да')
else:
    print('Нет')