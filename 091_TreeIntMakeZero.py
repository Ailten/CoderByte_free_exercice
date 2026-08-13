
# tree int make zero.
# /

# take a list of int, and return a range of number on it with sum made 0.


def rangeZero(arr: list[int]) -> list|None:

    arr.sort()

    start_i = 0
    end_i = len(arr)

    while True:
        total = sum(arr[start_i:end_i])
        if total == 0:
            return arr[start_i:end_i]
        if total < 0:
            start_i += 1
        else:
            end_i -= 1
        
        if start_i == start_i:
            return None
        
# need debug.


print(rangeZero([5,1,2,3,-1,0,2,-1,-2,3,2]))

