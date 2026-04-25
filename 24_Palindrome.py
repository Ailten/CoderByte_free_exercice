
# Palindrome (Easy).
# (?)

# return true if the string send is a palindrome (can be read in both direction).



def palindrome(word):

    return word == word[::-1]



print(palindrome('abc'))
print(palindrome('aba'))