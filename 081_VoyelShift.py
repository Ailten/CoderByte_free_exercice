
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


def voyelShiftV2(s: str) -> str:

    voyel_shift = {
        'a': 'e',
        'e': 'i',
        'i': 'o',
        'o': 'u',
        'u': 'y',
        'y': 'a'
    }

    for i in range(len(s)):
        new_voyel = voyel_shift.get(s[i], None)
        if new_voyel == None:
            continue
        s =  s[:i] + new_voyel + s[i+1:]

    return s


print(voyelShiftV2('thomas'))
print(voyelShiftV2('benois'))