def find_insert_position(array, x):
    left = 0
    right = len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left


array = [1, 2, 3, 3, 3, 5]
x = 4
print(find_insert_position(array, x))
