
# plus one.
# https://leetcode.com/problems/plus-one/



def plusOne(arr_int: list[int]) -> list[int]:

    is_add_one = True
    for i in range(len(arr_int)-1, -1, -1):  # loop on digit (from right to left).

        arr_int[i] = (arr_int[i] + 1) % 10  # increament (in range 0~9).

        if arr_int[i] != 0:  # if increment not overange, cut it.
            is_add_one = False
            break

    if is_add_one:  # if still need increament, insert a digit at left.
        arr_int.insert(0, 1)

    return arr_int



print(''.join([ str(e) for e in plusOne(  # 124.
    [1,2,3]
)]))
print(''.join([ str(e) for e in plusOne(  # 130.
    [1,2,9]
)]))
print(''.join([ str(e) for e in plusOne(  # 200.
    [1,9,9]
)]))
print(''.join([ str(e) for e in plusOne(  # 1000.
    [9,9,9]
)]))