
# Word Split (Medium).
# (?)

# take a string and a dictionary (list of word), and return true if the strig can be split in two word of the dictionary.


def wordSplit(word: str, words: list):
    for w in words:
        rest = word.replace(w, '')
        if rest in words:
            return True
    return False


print(wordSplit('aabb', ['aa', 'bb']))
print(wordSplit('aab', ['aa', 'bb']))
print(wordSplit('z-ab', ['aa', 'bb', 'ab', 'z']))
print(wordSplit('zab', ['aa', 'bb', 'ab', 'z']))