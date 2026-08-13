
# Array Addition I (Easy).
# (?)

# take an array of num, return true if two number in the array can be add to make the bigest into.


def arrayAdditionI(arr):

    bigest = max(arr)
    arr.remove(bigest)

    for i in range(len(arr)):
        a = arr[i]
        for j in range(i+1, len(arr)):
            b = arr[j]

            if a + b == bigest:
                return True
    
    return False




print(arrayAdditionI([1,2,3]))
print(arrayAdditionI([5,1,9,2,3,8]))
print(arrayAdditionI([1,2,32]))