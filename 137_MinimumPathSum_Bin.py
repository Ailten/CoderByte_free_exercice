
# Minimum path sum.
# https://leetcode.com/problems/minimum-path-sum/



def func(grid: list[list[int]]) -> int:

    def getByte(int_val: int, index_byte: int) -> bool:
        return (int_val >> index_byte) & 1 == 1

    def intToBin(int_val: int, length: int = 8):
        for i in range(length):
            yield getByte(int_val, i)

    def intToStrBin(int_val: int, length: int = 8):
        list_str_byte = []
        for i in range(length):
            list_str_byte.append('1' if getByte(int_val, i) else '0')
        return ''.join(list_str_byte)

    def binToInt(list_byte: list[bool]) -> int:
        output = 0
        for i in range(len(list_byte)):
            if list_byte[i]:
                output |= 1 << i
        return output
    
    def isMatchingOneCount(int_val: int, byte_expected: int, length: int = 8) -> bool:
        byte_count = 0
        for i in range(length):
            if getByte(int_val, i):
                byte_count += 1
        return byte_count == byte_expected
    

    amount_of_move_down_by_path = len(grid)-1
    amount_of_move_right_by_path = len(grid[0])-1
    amount_of_move_by_path = amount_of_move_down_by_path + amount_of_move_right_by_path
    path_int_start = binToInt([True]*amount_of_move_right_by_path + [False]*amount_of_move_down_by_path)
    path_int_end = binToInt([False]*amount_of_move_down_by_path + [True]*amount_of_move_right_by_path)

    min_sum_cel = float('inf')

    for current_path_int in range(path_int_start, path_int_end+1):
        if not isMatchingOneCount(current_path_int, amount_of_move_right_by_path, length=amount_of_move_by_path):
            continue

        # browse current path.
        current_pos = [0,0]
        current_sum_cel = grid[0][0]
        is_path_sum_to_big = False
        for index_move in range(amount_of_move_by_path):
            is_move_right = getByte(current_path_int, index_move)
            current_pos[1 if is_move_right else 0] += 1
            current_sum_cel += grid[current_pos[1]][current_pos[1]]

            if current_sum_cel > min_sum_cel:  # skip path when to big (even if it's not finish).
                is_path_sum_to_big = True
                break

        if is_path_sum_to_big:  # skip path (to big).
            continue

        min_sum_cel = current_sum_cel  # overide new shortest path.

    return min_sum_cel



print(func([  # 7.
    [1,1,1,2],
    [3,1,2,1],
    [1,1,1,1],
    [2,1,3,1],
]))