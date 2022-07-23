# Напишите программу, удаляющую из текста все слова, содержащие "абв".


print(''.join(input().lower().split('абв'))) # Это просто удаляет "абв"

print(' '.join([i for i in input().split() if 'абв' not in i.lower()])) # Это удаляет слово с "абв"


# Это развернутый метод для удаления слова, содержащего "абв"
stroka = input().split()
arr = [i for i in stroka if 'абв' not in i.lower()]
new_str = ' '.join(arr)
print(new_str)

# Привет как делабв