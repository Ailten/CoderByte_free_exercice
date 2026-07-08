
# Search 2D Matrix.
# https://leetcode.com/problems/search-a-2d-matrix/



def func(m: list[list[int]], target: int) -> bool:

    i_range = len(m) // 2
    i = i_range
    is_last_range = False

    while True:
        print(f'y: {i}')
        is_lower = target < m[i][0]
        is_upper = target > m[i][-1]
        if is_lower or is_upper:
            new_i_range = i_range // 2 + i_range % 2
            if is_last_range:
                return False
            if new_i_range == i_range:
                is_last_range = True
            i_range = new_i_range
            i += i_range if is_upper else -i_range
            continue
        break
    
    l = m[i]
    i_range = len(l) // 2
    i = i_range
    is_last_range = False

    while True:
        print(f'x: {i}')
        is_lower = target < l[i]
        is_upper = target > l[i]
        if is_lower or is_upper:
            new_i_range = i_range // 2 + i_range % 2
            if is_last_range:
                return False
            if new_i_range == i_range:
                is_last_range = True
            i_range = new_i_range
            i += i_range if is_upper else -i_range
            continue
        break

    return True
        
    

print(func([  # True.
    [1,5,9],
    [10,12,15],
    [22,27,28],
], 5))
print(func([  # False.
    [1,5,9],
    [10,12,15],
    [22,27,28],
], 7))


