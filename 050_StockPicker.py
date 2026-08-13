
# Stock Picker (Medium).
# (?)

# take an array of price at every hours of the day (for a product), eval what is the bigest benefice you can make (buy when it's low and sell when it's sheap).


def stockPicker(arr):

    return max(*arr) - min(*arr)


print(stockPicker([1,2,3]))
print(stockPicker([1,2,3,4]))
print(stockPicker([1,2,3,4,0,15]))