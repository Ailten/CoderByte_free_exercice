

# find a combinaison of numbers who made the max value in array.

def func(arr: list[int]) -> bool:

    max_val = max(arr)
    arr.remove(max_val)

    for i in range(2 ** len(arr) + 1):
        total = sum([ a for k,a in enumerate(arr) if (
            (i >> k) % 2 == 1
        )])
        if total == max_val:
            return True
    return False


print(func([-1, 3, 3, 5, 10]))
print(func([3, 3, 5, 8, 12]))