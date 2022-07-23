# В файле находится N натуральных чисел, записанных через пробел.
# Среди числе не хватает одного, что бы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


with open('file_for_018.txt', 'r') as file:
    list_1 = list(map(int, file.readline().split()))
    print(list_1)
    for i in range(1, len(list_1)):
        if list_1[i] - 1 != list_1[i - 1]:
            print((list_1[i - 1] + list_1[i]) // 2)
    file.close()