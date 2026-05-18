
# Voyel Shift (Easy)
# (/)

# Take a string and return it with all voyel replaced by the next one.


def voyelShift(s: str) -> str:

    voyels = ['a', 'e', 'i', 'o', 'u', 'y']

    for i in range(len(s)):
        if not s[i] in voyels:
            continue
        i_voyel = next([ i_v for i_v in range(len(voyels)) if s[i] == voyels[i_v]].__iter__(), None)
        i_voyel = i_voyel +1 % len(voyels)
        s = s[:i] + voyels[i_voyel] + s[i+1:]
    
    return s

print(voyelShift('thomas'))
print(voyelShift('benois'))