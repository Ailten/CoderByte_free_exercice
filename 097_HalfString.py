
# half string
# /

# take a string, return another fill of one char on two ('abcde' -> 'ace').

def evenStr(line: str) -> str:

    return ''.join([ c for i,c in enumerate(list(line)) if i % 2 == 0 ])



print(evenStr('abcde'))  # ace
print(evenStr('b-o-n-j-o-u-r'))  # bonjour