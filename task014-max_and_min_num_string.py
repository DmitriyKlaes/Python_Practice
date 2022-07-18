# Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

string_1 = '234 54 3 423 4'
list_1 = string_1.split()
max = int(list_1[0])
min = int(list_1[0])
for i in list_1:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)
print(f'{max} {min}')
        