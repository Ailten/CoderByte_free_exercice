
# Count Element Removed.
# /

# return the length of elemnets in an array whish is not equal to a value send.

def countElementRemoved(arr: list[int], num: int) -> int:

    return len([ e for e in arr if e != num])


print(countElementRemoved([1,2,1,3,1], 1))  # 2