
# Letter Challeng (Easy).
# (?)

# code cesar on a string, and upper case all voyel.

def LetterChanges(strParam):

    min_i = ord('a')
    max_i = ord('z')
    cesar_decalage = 1
    voyel = { 'a', 'e', 'i', 'o', 'u', 'y'}

    str_out = ''
    for char in strParam:
        index_ascii = ord(char)
        index_ascii += cesar_decalage

        while not index_ascii in range(min_i, max_i + 1):  # like modulo, in alphabet range.
            index_ascii += 26 if cesar_decalage < 0 else -26
        
        new_char = chr(index_ascii)
        if new_char in voyel:
            new_char = new_char.upper()
        
        str_out += new_char

    return str_out


print(LetterChanges('abc'))
print(LetterChanges('aazz'))
print(LetterChanges('aeiou'))
print(LetterChanges('tvwxyz'))