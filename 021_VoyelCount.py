import re

# Voyel Count (Easy).
# (?)

# count how many voyel in the string send.


def voyelCount(line):

    return len(re.findall('[aeiouy]', line))


print(voyelCount('-'))
print(voyelCount('---a---'))
print(voyelCount('abcde'))
print(voyelCount('aey'))