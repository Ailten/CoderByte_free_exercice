
# Simple Adding (Easy).
# (?)

# return fibonatchy sum of a num send.


def fibonatchySum(num):

    if num == 1:
        return 1
    
    return num + fibonatchySum(num - 1)





print(fibonatchySum(1))
print(fibonatchySum(2))
print(fibonatchySum(3))
print(fibonatchySum(4))
print(fibonatchySum(5))