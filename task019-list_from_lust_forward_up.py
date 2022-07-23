# Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя. 
# *Пример:* [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Мой вариант
# nums = [3, 1, 2, 3, 4, 6, 1, 7]
nums = [1, 5, 2, 3, 4, 6, 1, 7]
test = [nums[i] for i in range(len(nums)-1) if nums[i] < nums[i + 1] and nums[i] not in nums[:i]]
print(test)


# Первый вариант 
def get_up2(nums):
    ups = [nums[0]] 
    for i in nums: 
        if i > max(ups): 
            ups.append(i) 
    return ups 

print(get_up2(nums)) 

# Второй вариант
def get_up(nums): 
    ups = [] 
    for i in range(len(nums)): 
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups: 
            ups.append(nums[i]) 
    return ups 

print(get_up(nums))