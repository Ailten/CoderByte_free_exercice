
# Permutations
# https://leetcode.com/problems/permutations/

# take an array of int (max len 6), and return all variation of order can be made.


def func(arr: list[int]) -> list[list[int]]:

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    if len(arr) == 2: 
        return [[arr[0], arr[1]], [arr[1], arr[0]]]
    
    output = []
    for k,v in enumerate(arr):
        values_without_current = [ e for i,e in enumerate(arr) if i != k ]
        new_patterns = func(values_without_current)
        new_patterns = [ [v] + e for e in new_patterns ]
        output += new_patterns
    return output


print(len(func([])))  # 0.
print(len(func([0])))  # 1.
print(len(func([0,1])))  # 2.
print(len(func([0,1,2])))  # 6.
print(len(func([0,1,2,3])))  # 24.
print(len(func([0,1,2,3,4])))  # 120.
print(len(func([0,1,2,3,4,5])))  # 720.
