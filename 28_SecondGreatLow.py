
# Second Great Low (Easy).
# (?)

# take an array of num, and return the second lowest and second bigest (in string format, separate by a space).


def secondGreatLow(arr):

    # TODO: verify if there is at least 3 (or 4) distinct values in array before.

    arr.sort()
    return f'{arr[1]} {arr[len(arr)-2]}'


print(secondGreatLow([1,2,3,4,5,6,7,8,9]))
print(secondGreatLow([1,2,3,4]))
print(secondGreatLow([1,2,3]))