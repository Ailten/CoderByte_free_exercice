import re

# Word Count (Easy).
# (?)

# count how many word (separate by space) in a string send.


def wordCount(line):

    return len(re.findall('[^ ]{1,}', line))


print(wordCount('   '))
print(wordCount('hello'))
print(wordCount('hello word'))
print(wordCount('a b c'))