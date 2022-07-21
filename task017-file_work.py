file = open('file_for_017.txt', 'r', encoding='utf-8')
print(file.readlines())

with open('file_for_017.txt', 'a', encoding='utf-8') as file:
    file.write('\n6')