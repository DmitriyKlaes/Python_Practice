# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def search_enter(arr, string):
    count = 0
    for i in range(len(arr)):
        if arr[i] == string:
            count += 1
        if count == 2:
            return f'yes: {i + 1}'
    return 'no'


list_1 = ['qwerty', 'asd', 'zxc', 'qwerty', 'sdfgsdf']
print(search_enter(list_1, 'qwerty'))
