
# Substring Matcher (Medium).
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

# take a string, return que quantity of substring who is "correct" (= at least 4 character and start-end with the same char), and do not contain a substring who's correct.


# TODO: debug. (no \k in python), and regex less gready skip "ccdc".

import re

def maxSubstrings(word: str) -> int:
    return len([ m[0] for m in matchRegex(word) if len(matchRegex(m[0])) == 1 ])

	#count = 0
	#
	#letters = set(word)
	#while True:
	#
	#	m = re.search(r'^.{0,}?((.).{2,}?\2)', word)
	#	if m == None:
	#		return count
	#	count += 1
	#	print(m.group())
	#	word = word[len(m.group()):]
	#	print(word)


def matchRegex(word: str) -> int:
	return re.findall(r'((.).{2,}?\2)', word)


#print(maxSubstrings('abcdeafdef'))  # 2 -> "abcdea" and "fdef"
print(maxSubstrings("aabececbbeccdcdcdbdece"))  # "bececb" "ccdc" et "cbbdec"