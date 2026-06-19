
# jump game 2.
# https://leetcode.com/problems/jump-game-ii/

# take an array of int.
# start at index 0.
# return the less amount of jump to reach the last cel.
# eatch cell you step has an int number, it represent the bigest range jump you can make.
# (in this example, the array can always be solv, if you want, return -1 if no solution).


#  -- bad vertion : solv but do not wrong algo, do not return the shortest path (see the first test case).
#def func(arr: list[int]) -> int:
#
#    current_index = 0
#    jump_count = 0
#    index_browse = {0}  # for back-track.
#    jump_path = []  # for back-track.
#
#    while current_index != len(arr) - 1:
#        current_int = arr[current_index]
#        range_allow = [ (k,v) for k,v in enumerate(arr) if (
#            (  # take index allow to jump.
#                k > current_index and
#                k <= current_index + current_int
#            ) and
#            not k in index_browse  # remove index already brows.
#        ) ]
#
#        if len(range_allow) == 0:  # if can't reach the end with this path, back-track.
#            jump_count -= 1
#            if jump_count == -1:
#                return -1  # return -1 if there is no path to solv.
#            current_index = jump_path.pop()
#            continue
#
#        jump_path.append(current_index)
#        next_cel_jump = range_allow.pop()
#        current_index = next_cel_jump[0]
#        index_browse.add(current_index)
#        jump_count += 1
#
#    return jump_count

def func(arr: list[int]) -> int:

    index_reach = {0}
    jump_count = 0

    while not len(arr) -1 in index_reach:
        next_reach = set()

        for ir in index_reach:
            value_ir = arr[ir]
            if value_ir <= 0:
                continue
            next_reach |= set(range(ir+1, ir+value_ir+1))

        if len(next_reach) == 0:  # can't be solv.
            return -1

        jump_count += 1
        index_reach = next_reach

    return jump_count



print(func([2,3,1,1,4]))  # 2.  -> index 0, +1 + 3  == last index (in two jumps).
print(func([1,2,3,0,2,0,9]))  # 4.  -> 2,3,2,9
print(func([1,3,0,0,0,9]))  # -1