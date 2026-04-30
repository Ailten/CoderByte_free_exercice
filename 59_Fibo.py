
# Fibo (Easy).
# (?)

# make a function calcul fibonachy for a n send.



def f(n):
    if n == 1 or n == 0:
        return n
    
    cash = [0, 1]
    for i in range(2, n+1):
        cash[i%2] = sum(cash)
        if i == n:
            return cash[i%2]
        

print(f(0))  # 0.
print(f(1))  # 1.
print(f(2))  # 1.
print(f(3))  # 2.
print(f(4))  # 3.
print(f(5))  # 5.
print(f(6))  # 8.