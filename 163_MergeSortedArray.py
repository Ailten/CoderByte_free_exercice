
# merge sorted array
# https://leetcode.com/problems/merge-sorted-array/


def merge(nums1: list[int], len_nums1: int, nums2: list[int], len_nums2: int) -> list[int]:

    i1 = 0
    i2 = 0
    while True:
        if i2 == len_nums2:  # break if all nums2 is fit.
            break
        if i1 == len_nums1:  # fit all nums2 at end.
            for i in range(0, len(nums2)-i2):
                nums1[i1+i] = nums2[i2+i]
            break

        # get both values.
        v1 = nums1[i1]
        v2 = nums2[i2]

        # debug.
        #print(f'{nums1} -> {v1}')
        #print(f'{nums2} -> {v2}')
        #print(f"- {v1}, {v2}")

        # already good order.
        if v1 <= v2:
            i1 += 1
            continue

        # insert from nums2.
        for i in range(i1, len(nums1)):
            v1 = nums1[i]
            nums1[i] = v2
            v2 = v1

        i2 += 1
        i1 += 1
        len_nums1 += 1
        
    return nums1

# --- test.
#print(merge([1,0], 1, [2], 1))  # [1,2].
#print(merge([1,0,0], 1, [2,3], 2))  # [1,2,3].
#print(merge([1,3,0], 2, [2], 1))  # [1,2,3].
#print(merge([1,3,4,0], 3, [2], 1))  # [1,2,3,4].
#print(merge([1,4,5,0,0], 3, [2,3], 2))  # [1,2,3,4,5].
#print(merge([1,0,0,0], 1, [2,3,4], 3))  # [1,2,3,4].
#print(merge([1,4,0,0], 2, [2,3], 2))  # [1,2,3,4].

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))  # [1,2,2,3,5,6].