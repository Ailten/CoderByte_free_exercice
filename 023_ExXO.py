import re

# Ex XO (Easy).
# (?)

# take a string, return true if there is an equal amount of char "x" and char "o".


def exXO(line):

    x_count = len(re.findall('[x]', line))
    o_count = len(re.findall('[o]', line))

    return x_count == o_count


print(exXO('------'))
print(exXO('-x--o-'))
print(exXO('xx------oo'))
print(exXO('xoxoxo'))
print(exXO('xxoxoo_xo'))
print(exXO('---x---oo-'))