
# sliding max window.
# find the max value in an array, but you have to browse it by a window defined.

def func(arr: list[int], k: int) -> int:

    max_value = None
    for i in range(len(arr) - (k-1)):
        window = arr[i:i+k]
        if max_value == None:
            max_value = max(window)
        elif window[-1] > max_value:
            max_value = window[-1]

    return max_value
            

print(func([1,2,3,4,5], 2)) # 5