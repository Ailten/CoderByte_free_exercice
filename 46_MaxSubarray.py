
# Max Subarray (Medium).
# (?)

# take an array of int (positif and negatif), return the sum of the sub array having the bigest result.

def maxSubarray(arr: list) -> int:

    max_sum = arr[0]
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            sum_sub_array = sum(arr[i:j+1])
            if sum_sub_array > max_sum:
                max_sum = sum_sub_array
    return max_sum


print(maxSubarray([1,2,3]))
print(maxSubarray([1,2, -9, 1]))
print(maxSubarray([1,2, -9, 4]))