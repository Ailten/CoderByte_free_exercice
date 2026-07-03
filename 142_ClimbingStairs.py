
# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/


def func(steps_stair: int) -> int:

    if steps_stair <= 2:
        return steps_stair
    
    way_valid_count = 0

    way = {('1', 1), ('2', 2)}

    while len(way) != 0:
        new_way = set()
        
        for w in way:
            for i in range(1, 3):
                new_current_way = (
                    w[0] + str(i), 
                    w[1] + i
                )
                if new_current_way[1] > steps_stair:
                    continue
                if new_current_way[1] == steps_stair:
                    # print(f'- {new_current_way[0]}')  # debug, print all valid way.
                    way_valid_count += 1
                    continue
                new_way.add(new_current_way)

        way = new_way
    
    return way_valid_count



print(func(0))  # 0.
print(func(1))  # 1.
print(func(2))  # 2.
print(func(3))  # 3.
print(func(4))  # 5.
print(func(5))  # 8.