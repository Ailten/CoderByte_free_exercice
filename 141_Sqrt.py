
# Sqrt
# https://leetcode.com/problems/sqrtx/


def sqrt(val: int) -> int:

    if val <= 1:
        return val
    
    last_i = 0
    for i in range(1, val+1):
        if (i * i) > val:
            return last_i
        last_i = i
        
    raise Exception('error')


print(sqrt(0))  # 0.
print(sqrt(1))  # 1.
print(sqrt(2))  # 1.
print(sqrt(3))  # 1.
print(sqrt(4))  # 2.
print(sqrt(5))  # 2.
print(sqrt(6))  # 2.
print(sqrt(7))  # 2.
print(sqrt(8))  # 2.
print(sqrt(9))  # 3.
    