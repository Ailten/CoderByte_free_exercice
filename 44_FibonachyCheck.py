
# Fibonachy Check (Medium).
# (?)

# take a number, and verify if it was contained in fibonachy suite.

def fibonachyCheck(value):

    i = 0
    fibonachy = 0
    while True:
        i += 1
        fibonachy += i

        if value == fibonachy:
            return True
        elif fibonachy > value:
            return False


print(fibonachyCheck(1))
print(fibonachyCheck(2))
print(fibonachyCheck(3))
print(fibonachyCheck(4))
print(fibonachyCheck(5))
print(fibonachyCheck(6))