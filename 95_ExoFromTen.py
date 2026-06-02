import re

# _____________________________________________________>>

# take a string of number (2-9), return true if the string contain a suit of N character "N" (22 333 ...) at least one.
def exo01(line: str) -> bool:
    for i in range(2, 10):
        if re.search('['+str(i)+']{'+str(i)+'}', line) != None:
            return True
    return False

print('_____________')
print(exo01('123456'))  # false.
print(exo01('123334'))  # true.

# _____________________________________________________>>

# take a string (with an aster in center), return a string of alternance of both char of the both side of the input.
def exo02(line: str) -> str:

    line_split = line.split('*')

    if len(line_split[0]) != len(line_split[1]):
        raise Exception('not valide')

    output = ''
    for i in range(len(line_split[0])):
        output += line_split[0][i] + line_split[1][i]
    return output

print('_____________')
print(exo02('aaa*bbb'))  # ababab.
print(exo02('123*456'))  # 142536.

# _____________________________________________________>>

# return the sum of the 4 bigest number in an array.
def exo03(arr: list[int]) -> int:

    arr.sort()
    arr = arr[-4:]
    return sum(arr)

print('_____________')
print(exo03([1,2,3,4]))  # 10.
print(exo03([4,5,6,7,8]))  # 26.

# _____________________________________________________>>

# take a string, and return a list of char (without the doublon).
def exo04(line: str) -> list[str]:

    output = []
    for char in line:
        if char in output:
            continue
        output.append(char)
    return output

print('_____________')
print(exo04('aabbcc'))  # [a,b,c].
print(exo04('aaaabb'))  # [a,b].

# _____________________________________________________>>


# dispatch number on a triangle equilateral, find if the nuber send is a valid triange or not (fibonachi or not).

# with loop.
#def exo05(input: int) -> bool:
#
#    i = 1
#    agreg = 0
#    while True:
#        agreg += i
#        if agreg == input:
#            return True
#        if agreg > input:
#            return False
#        i += 1

# with recursive + lru_cache.
from functools import lru_cache
@lru_cache
def fibonachi(n: int) -> int:
    if n <= 1:
        return n
    return fibonachi(n-2) + fibonachi(n-1)

def exo05(input: int) -> bool:
    
    i = 1
    while True:
        fi = fibonachi(i)
        if fi == input:
            return True
        if fi > input:
            return False
        i += 1


print('_____________')
print(exo05(6))  # true
print(exo05(8))  # false

# _____________________________________________________>>


# sort an array of int (asc), but stray all odd (%2) number at their current position.
def exo06(input: list[int]) -> list[int]:

    odds = { k:v for k,v in enumerate(input) if v % 2 == 0 }
    input = [ v for v in input if v % 2 != 0]
    input.sort()
    for k,v in odds.items():
        input = input[:k] + [v] + input[k:]
    return input


print('_____________')
print(exo06([5,2,3,4]))  # 3,2,5,4
print(exo06([3,9,8,7]))  # 3,7,8,9

# _____________________________________________________>>


# take a string, replace all char by '(', unless the char is ocur many time in the string (then ')'), case insenssitive.
def exo07(input: str) -> str:

    input = input.lower()

    output = ''
    for char in input:
        if len(re.findall(char, input)) > 1:
            output += ')'
            continue
        output += '('
    return output


print('_____________')
print(exo07('abc'))  # (((
print(exo07('aabcc'))  # ))())

# _____________________________________________________>>


from functools import reduce

# take an array of int, return the same array, but all cell is the multiplycation result of all value (unless the one at this index).
def exo08(input: list[int]) -> list[int]:

    # with mult allow.
    #mult = reduce(lambda acc, e: acc * e, input, 1)
    #return [ int(mult / e) for e in input ]

    return [ (
        reduce(lambda acc, e: acc * e, input[:k]+input[k+1:], 1)
    ) for k,v in enumerate(input) ]
        

print('_____________')
print(exo08([1,2,3]))  # 6,3,2
print(exo08([4,5,6]))  # 30,24,20

# _____________________________________________________>>

def exo09(input: list[int]) -> list[int]:

    return [ (
        'fizzbuzz' if (e % 5 == 0 and e % 3 == 0) else
        'fizz' if (e % 3 == 0) else
        'buzz' if (e % 5 == 0) else
        e
    ) for e in range(1, input+1)]

print('_____________')
print(exo09(5))  # 1,2,fizz,4,buzz
print(exo09(15))  # 1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz

# _____________________________________________________>>

# return true if the string input is contains all char alphabet (26 ones), input is always in lowercase.
def exo10(input: str) -> bool:

    arr = list({ ord(c) for c in input })
    arr = [ a for a in arr if a >= ord('a') and a <= ord('z') ]
    arr.sort()
    return ''.join([ chr(a) for a in arr ]) == 'abcdefghijklmnopqrstuvwxyz'


print('_____________')
print(exo10('abc'))  # false
print(exo10('abcdefghijklmnopqrstuvwxyz'))  # true

# _____________________________________________________>>

# return true if both interval is overlaping. ('1-13' and '5-32' -> true)
def exo11(input_a: str, input_b: str) -> bool:

    end_a = input_a.split('-')[1]
    start_b = input_b.split('-')[0]
    return end_a <= start_b


print('_____________')
print(exo11('1-12', '5-30'))  # true
print(exo11('1-5', '10-15'))  # false

# _____________________________________________________>>

# remove suplicate char consecutive ('aaabb' -> 'ab')
def exo12(input: str) -> str:

    return re.sub(r'(.)\1*', r'\1', input)


print('_____________')
print(exo12('aaabb'))  # ab
print(exo12('aaaabbbbbcc'))  # abc

# _____________________________________________________>>

# remove suplicate char consecutive ('aaabb' -> 'ab')
def exo12(input: str) -> str:

    return re.sub(r'(.)\1*', r'\1', input)


print('_____________')
print(exo12('aaabb'))  # ab
print(exo12('aaaabbbbbcc'))  # abc

# _____________________________________________________>>

# take a string (letter separate by many '*', split it, and merge it consecutively : "aaa*bbb*ccc" -> "abcabcabc").
def exo12(input: str) -> str:

    arr = input.split('*')
    output = ''
    for i in range(len(arr[0])):
        output += ''.join([ a[i] for a in arr])
    return output

print('_____________')
print(exo12('aaa*bbb*ccc'))  # abcabcabc
print(exo12('abc*abc*abc'))  # aaabbbccc



#concatenate string separate by * ex : "aaa*bbb*ccc" -> "abcabcabc"