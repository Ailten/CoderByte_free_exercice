
# Insert Interval.
# https://leetcode.com/problems/insert-interval/

# take a list of interval (start, end as int), and insert a new interval on it (if nessesar, merge intervals overlaping).
# the intervals inputs ar not overlaping and already sorted by start.

from functools import reduce
from enum import IntEnum

def func(intervals: list[list[int]], insert_inerval: list[int]) -> list[list[int]]:

    if len(intervals) == 0:
        intervals.append(insert_inerval)
        return intervals

    def isOverlaping(a: list[int], b: list[int]) -> bool:
        """
        Check if two interval is overlaping.
        """
        if a[0] > b[0]:
            (a,b) = (b,a)
        return b[0] <= a[1] and a[0] <= b[1]
    
    def mergeInterval(a: list[int], b: list[int]) -> list[int]:
        """
        Merge two interval (take min start and max end).
        """
        return [
            min(a[0], b[0]),
            max(a[1], b[1])
        ]

    class InsertState(IntEnum):
        before_match = 0,
        durring_match = 1,
        after_match = 2

    # already sorted.
    # already non-overlaping.

    i = 0
    insert_state = InsertState.before_match
    merged_interval = [insert_inerval[0], insert_inerval[1]]
    while i < len(intervals):
        interval = intervals[i]

        is_overlaping = isOverlaping(merged_interval, interval)

        if is_overlaping and insert_state == InsertState.before_match:
            insert_state = InsertState.durring_match
        elif not is_overlaping and insert_state == InsertState.durring_match:
            insert_state = InsertState.after_match
            intervals.insert(i, merged_interval)
            break

        if insert_state == InsertState.durring_match:
            merged_interval = mergeInterval(merged_interval, interval)
            intervals.pop(i)
            continue
        
        i += 1

    if insert_state == InsertState.before_match:
        intervals.insert(0, merged_interval)
    elif insert_state == InsertState.durring_match:
        intervals.append(merged_interval)

    return intervals



print(func([], [1,2]))  # [[1,2]].  --> empty base list.
print(func([[3,4]], [1,2]))  # [[1,2],[3,4]].  --> insert without any overlaping.
print(func([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]].  --> overlaping before.
print(func([[2,5],[6,9]], [1,3]))  # [[1,5],[6,9]].  --> overlaping after.
print(func([[1,3],[4,6]], [2,5]))  # [[1,6]].  --> duple overlaping.
print(func([[1,3],[4,6],[7,9]], [2,8]))  # [[1,9]].  --> tripple overlaping.
print(func([[1,2],[3,5]], [4,6]))  #  [[1,2],[3,6]]  --> merge in last element.
print(func([[2,4],[8,9]], [1,3]))  #  [[1,4],[8,9]]  --> merge in first element.
print(func([[1,2]], [2,3]))  #  [[1,3]]  --> border (last).
print(func([[2,3]], [1,2]))  #  [[1,3]]  --> border (first).