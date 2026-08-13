
# Mean Mode (Easy)
# (?)

# return true if the moyen and the mode of an array of num, is equal.


def meanMode(arr):

    arr.sort()

    mean = sum(arr) / len(arr)
    mode = arr[len(arr) // 2]

    return mean == mode


print(meanMode([1,2,3]))
print(meanMode([1,2,15]))