
# Primary Number (Medium).
# (?)

# take a num and return True if it's primary (only divide by one and it self).

def primaryNum(num: int) -> bool:

    if num == 1:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(primaryNum(1))
print(primaryNum(2))
print(primaryNum(3))
print(primaryNum(4))
print(primaryNum(5))
print(primaryNum(6))
print(primaryNum(7))