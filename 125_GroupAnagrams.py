
# Group Anagrams.
# https://leetcode.com/problems/group-anagrams/

# take a list of string, return a list of group (list) of string with the same letters.
# regardless of order groups.


def func(words: list[str]) -> list[list[str]]:

    dico_anagram: dict[str, list[str]] = dict()

    for word in words:

        letter_arr = list(word)  # generate an unique key setializable.
        letter_arr.sort()
        key = ''.join(letter_arr)

        if not key in dico_anagram:  # insert or update the list (to append the word).
            dico_anagram[key] = [word]
        else:
            dico_anagram[key].append(word)
        
    return list(dico_anagram.values())



print('< result 1 >')
value = ["eat","tea","tan","ate","nat","bat"]
print(func(value))  # [["bat"],["nat","tan"],["ate","eat","tea"]]

print('< result 2 >')
value = []
print(func(value))  # []

print('< result 3 >')
value = ["a"]
print(func(value))  # [["a"]]