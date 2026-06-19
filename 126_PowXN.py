
# Pow x n.
# https://leetcode.com/problems/powx-n/

# implement a function, who return the result of X pow N (exposent N).


def my_pow(x: float, n:int) -> float:

    if n == 1:
        return x
    if n == 0:
        return 1.0
    
    if n > 0:
        output = x
        for _ in range(n - 1):
            output *= x
        return output
    
    return 1 / my_pow(x, abs(n))



print(my_pow(2.0, 2))  # 4
print(my_pow(2.0, 1))  # 2
print(my_pow(2.0, 0))  # 1

print(my_pow(2.0, 10))  # 1024
print(my_pow(2.1, 3))  # 9.261
print(my_pow(2.0, -2))  # 0.25