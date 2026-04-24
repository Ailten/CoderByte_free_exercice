
# First Factorial (easy).
# https://coderbyte.com/information/First%20Factorial

def FirstFactorial(num):

  if num == 1:
    return 1
    
  return FirstFactorial(num - 1) * num

# keep this function call here 
print(FirstFactorial(4))