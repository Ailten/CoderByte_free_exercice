
# Longest SUbstring (Medium).
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# return the length of the bigest substring without doublon char on it.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def getIndexDuplicateChar(line: str) -> int|None:
            dico = {}
            for j in range(len(line)):
                char = line[j]
                if not char in dico:
                    dico[char] = j
                    continue
                return dico[char]
            return None
                
    
        if s == '':
            return 0

        i = 0
        j = 1
        max_len_find = 0
        while True:
            range_s = s[i:j]
            index_duplicate = getIndexDuplicateChar(range_s)
            if index_duplicate == None:
                if len(range_s) > max_len_find:
                    max_len_find = len(range_s)
            else:
                i += index_duplicate + 1
            j += 1
            if j > len(s):
                break
        return max_len_find


#print(lengthOfLongestSubstring(""))
#print(lengthOfLongestSubstring("a"))
#print(lengthOfLongestSubstring("au"))
#print(lengthOfLongestSubstring("bbbbbbbb"))
#print(lengthOfLongestSubstring("pwwkew"))
#print(lengthOfLongestSubstring("bbtablud"))