
# Merge Interval.
# https://leetcode.com/problems/merge-intervals/

# take an array of interval (start, end as int), and return an array of interval merged (when many interval is overlaping).


def func(intervals: list[list[int]]) -> list[list[int]]:

    if len(intervals) == 0:
        return intervals

    # order data.
    intervals.sort(key=lambda i: i[0])

    last_interval = intervals[0]

    i = 1
    while i < len(intervals):
        interval = intervals[i]

        if last_interval[1] >= interval[0]:
            if interval[1] > last_interval[1]:
                last_interval[1] = interval[1]
            intervals.pop(i)
            continue

        last_interval = interval

        i += 1

    return intervals



print(func([[1,3],[2,4],[5,7]]))  # [[1,4],[5,7]]
print(func([[1,2],[4,7]]))        # [[1,2],[4,7]]
print(func([[1,4],[2,8],[3,5]]))  # [[1,8]]
print(func([]))                   # []
