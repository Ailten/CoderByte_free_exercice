
# Alphabet Soup (Easy).
# (?)

# take a line, and order char by alphabetic order.


def alphabetSoup(line):
    arr_char = [ c for c in line ]
    arr_char.sort(key=lambda c: ord(c))
    return ''.join(arr_char)


print(alphabetSoup('abc'))
print(alphabetSoup('cba'))
print(alphabetSoup('cab'))