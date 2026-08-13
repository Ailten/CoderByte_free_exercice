import re

# Number Search (Easy).
# (?)

# Have the function NumberSearch(str) take the str parameter, search for all the numbers in the string, add them together, then return that final number divided by the total amount of letters in the string.


def numberSearch(line):

    total_num = sum([ int(e) for e in re.findall('[0-9]', line) ])
    amount_of_letter = len(re.findall('[a-z]', line, re.I))

    if amount_of_letter == 0:
        #raise ZeroDivisionError()  # TODO: prevent this exception properly.
        return total_num

    return total_num / amount_of_letter


print(numberSearch('1234'))
print(numberSearch('1234_a'))
print(numberSearch('1234_ab'))
print(numberSearch('_ab'))


