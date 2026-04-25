
# Check Num (Easy).
# (?)

# take two number, if first is lower return true, else return false, if it's equal return -1.


def checkNum(a, b):

    if a == b:
        return -1
    return a < b




print(checkNum(1, 2))
print(checkNum(2, 1))
print(checkNum(1000, 1001))
print(checkNum(2, -2))
print(checkNum(1, 1))