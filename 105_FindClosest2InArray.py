
# take an array of int (values 0,1,2), find the 1, and return the distance from the 1 to the closest 2. return zero if no 2.


def func(arr: list[int]) -> int:

    index_one = next([ k for k,a in enumerate(arr) if a == 1 ].__iter__(), None)
    if index_one == None:
        return 0
    
    count = 1
    while True:

        id_right = index_one + count
        if id_right < len(arr) and arr[id_right] == 2:
            return count
        
        id_left = index_one - count
        if id_left >= 0 and arr[id_left] == 2:
            return count
        
        if id_left < 0 and id_right >= len(arr):
            break

        count += 1

    return 0



print(func([0,0,0,1,0,0,0,2]))  # 4.
print(func([0,2,0,1,0,0,0,2]))  # 2.
print(func([0,2,0,1,2,0,0,2]))  # 1.
print(func([0,2,0,2,2,0,0,2]))  # 0.
print(func([0,0,0,1,0,0,0,0]))  # 0.