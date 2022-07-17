
# def random_number():
#     mili_second = int(round(time.time() * 10000))
#     new_random = str(mili_second)
#     result = int(new_random[10:-1]) // 10
#     return result

# print(random_number())





import time

print(str(time.time_ns())[-5:-3]) # + str(time.time_ns())[-3])