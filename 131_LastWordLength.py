
# Lenght of last word.
# https://leetcode.com/problems/length-of-last-word/

# get a string (sentence), and return the length of the last word.

def func(sentence: str) -> int:

    if sentence == '':
        return 0

    return len(sentence.split(' ')[-1])


print(func('bonjour thomas'))  # 6.
print(func(''))  # 0.
print(func('test un test deux test trois'))  # 5.