
# Longest Increasing Sequence (Medium).
# (?)

# take an array of int, return the largest sub array who is strictly increasing, return the length only.


def longestIncreasingSequence(arr):
    
    bigest_range_increasing = 1
    count_increasing = 1
    last_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > last_element:
            count_increasing += 1
        else:
            if count_increasing > bigest_range_increasing:
                bigest_range_increasing = count_increasing
            count_increasing = 1
        last_element = arr[1]
    
    if count_increasing > bigest_range_increasing:  # FIXME: doublon.
        bigest_range_increasing = count_increasing

    return bigest_range_increasing



print(longestIncreasingSequence([1,2,3]))
print(longestIncreasingSequence([1,0,2,3]))
print(longestIncreasingSequence([1,2,3,-1,4,5,6]))
print(longestIncreasingSequence([1,2,3,-1,4,5,6,10,2,3,4]))