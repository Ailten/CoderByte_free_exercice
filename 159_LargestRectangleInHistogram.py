
# largest retangle in histogram.
# https://leetcode.com/problems/largest-rectangle-in-histogram/


def func(h: list[int]) -> int:

    if len(h) == 0:
        return 0
    if len(h) == 1:
        return h[0]
    
    min_h = min(h)
    max_h = max(h)

    max_era = min_h * len(h)

    for hi in range(min_h+1, max_h +1):  # loop on every possible height (hi) as side rectangle.

        i = 0
        count_h = 0
        while i < len(h):  # loop on every h for find those who has the right hight (hi) or more.

            if h[i] >= hi:
                while i<len(h) and h[i]>=hi:  # loop on valire range h, to eval max rectangle of this height (hi).
                    count_h += 1
                    i += 1
                era = hi * count_h  # eval the era of the rectangle finde.
                if era > max_era:
                    max_era = era
                count_h = 0

            i += 1
        
    return max_era



print(func([2,4]))  # 4.
print(func([2,1,5,6,2,3]))  # 10.
