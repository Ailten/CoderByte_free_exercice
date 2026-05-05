
import re

# Substring Matcher (Medium).
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

# take a string, return que quantity of substring who is "correct" (= at least 4 character and start-end with the same char), and do not contain a substring who's correct.


# TODO: debug. (no \k in python), and regex less gready skip "ccdc".


# favorit vertion (but no \k in regex python, also not working well).
#def maxSubstrings(word: str) -> int:
#    return len([ m[0] for m in matchRegex(word) if len(matchRegex(m[0])) == 1 ])
#def matchRegex(word: str) -> int:
#	 return re.findall(r'((.).{2,}?\2)', word)


# time limite exceed.
def maxSubstrings(word: str) -> int:

	count = 0
	letters = set(word)

	while True:

		closests = []
		for l in letters:
			regex = l + r'.{2,}?' + l
			match = re.search(regex, word)
			if match == None:
				continue
			closests.append(match)

		if len(closests) == 0:
			break

		closests.sort(key=lambda m: len(m.group()) + m.start())
		closest = closests[0]

		count += 1
		print(closest.group())
		word = word[closest.start() + len(closest.group()):]


	return count
	





#print(maxSubstrings('abcdeafdef'))  # 2 -> "abcdea" and "fdef"
print(maxSubstrings("aabececbbeccdcdcdbdece"))  # "bececb" "ccdc" et "cbbdec"