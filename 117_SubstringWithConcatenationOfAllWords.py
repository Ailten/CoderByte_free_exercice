
# substring with concatenation of all words
# hard

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import re

def func(s: str, words: list[str]) -> list[int]:

    output = []

    all_words_len = sum([ len(w) for w in words ])
    for i in range(len(s) - (all_words_len - 1)):
        current_range_s = s[i: i + all_words_len]

        words_to_place = words.copy()
        words_to_place.sort(key=lambda w: len(w), reverse=True)

        while len(words_to_place) > 0:

            key_word, starting_word = next([ (k, w) for k,w in enumerate(words_to_place) if re.search(r'^'+w, current_range_s) != None ].__iter__(), (None, None))
            if starting_word == None:
                break
            current_range_s = current_range_s[len(starting_word):]
            words_to_place.pop(key_word)
            if len(words_to_place) == 0:
                output.append(i)
                break

    return output
            


print(func("barfoothefoobarman", ["foo","bar"]))  # -> [0,9].
print(func("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # -> [].

print(func("barfoofoobarthefoobarman", ["bar","foo","the"]))  # -> [6,9,12].

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].