
# Longest Palindrom (Medium).
# https://leetcode.com/problems/longest-palindromic-substring/

# take a string, return the longest palindrom in it.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = len(s)
        while True:

            for i in range(len(s) - l + 1):

                range_s = s[i:i+l]
                if self.isPalindrom(range_s):
                    return range_s

            l -= 1


    def isPalindrom(self, line: str) -> bool:
        return line == line[::-1]