import re

# Palindrome 2 (Medium).
# (?)

# verify if the string send is a palindrome (can be read in both direction), regardless of axent, special char, or casse (lower-upper).

def palindrome2(line):
    line_clean = re.sub('[^a-z]', '', line.lower())
    return line_clean == line_clean[::-1]


print(palindrome2('abc'))
print(palindrome2('aba'))
print(palindrome2('ab(c'))
print(palindrome2('abA'))