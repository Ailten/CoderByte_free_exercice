import re

# String Scramble (Medium).
# (?)

# create a function who take two argument (str), and verify if the first is containd in the second.

def stringScramble(str_search, str_container):

    # FIXME: re.match not working well during test. unknow reason.
    return len(re.findall(str_search, str_container)) > 0


print(stringScramble('a', 'aaa'))
print(stringScramble('abc', 'aabcaac'))
print(stringScramble('ab-c', 'aabcaac'))