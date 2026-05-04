
# Palindrom Number (Easy).
# https://leetcode.com/problems/palindrome-number/

# return if yes or no, a number send (int) is a "palindrom" (ex: 121).



class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_s = str(x)
        return x_s == x_s[::-1]