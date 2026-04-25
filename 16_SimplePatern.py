import re

# Simple Patern.
# (?)

# take a string, return true if eatch letter alphabetic has a char '+' before and after.



def simplePatern(line):

    return re.search('([^+][a-z]|[a-z][^+])', line) == None



print(simplePatern('abc'))
print(simplePatern('+a+b+++c+'))
print(simplePatern('$*-_+a+__-'))
print(simplePatern('-a-'))
print(simplePatern('---'))