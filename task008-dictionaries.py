# Словари

# number = {'Ivan': 987654987,
#           'Dima': 45542231}
# print(list(number.keys()))
# print(list(number.values()))
# print(list(number.items()))

# number[0] = 16
# print(number)


a = int(input())
n = {}
for i in range(a):
    n[i + 1] = (i+1) * 3 + 1
print(n)