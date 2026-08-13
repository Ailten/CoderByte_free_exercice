
# Dash Insert (Easy).
# (?)

# take a string, and insert '-' between two off number char.


def dashInsert(line):

    # TODO : verify if chars is number.

    i = 1
    while i < len(line):  # do a while instead of for, to edit the string it self.

        if int(line[i]) % 2 == 1 and int(line[i-1]) % 2 == 1:
            line = line[:i] + '-' + line[i:]
            i += 1

        i += 1

    return line


print(dashInsert('22222'))
print(dashInsert('2211222'))
print(dashInsert('221222'))
print(dashInsert('221122532'))