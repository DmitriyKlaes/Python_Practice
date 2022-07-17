def search_list(arr, number):
    if str(number) in arr:
        return 'yes'
    return 'no'

list_1 = ['Hello', '12', 'red', '567']
print(search_list(list_1, 12))