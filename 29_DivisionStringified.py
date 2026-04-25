
# Division Sitrngified (Easy).
# (?)

# take a big number, and return into a string, with character separate the tousent (and more).


def divisionStringified(num):

    str_out = ''
    i = 0
    for char in str(num)[::-1]:
        str_out = char + str_out
        if i == 2:
            str_out = ',' + str_out
        i = (i + 1) % 3

    if str_out[0] == ',':
        str_out = str_out[1:]
    
    return str_out




print(divisionStringified(100))
print(divisionStringified(1000))
print(divisionStringified(100000))
print(divisionStringified(1000000))