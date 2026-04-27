import re

# Run Length (Medium).
# (?)

# take a string, and return it compressed ('aaabb' -> '3a2b').

def runLength(line):

    line_out = ''
    while len(line) > 0:
        char_processing = line[0]
        i = 1
        while i < len(line):
            if line[i] != char_processing:
                break
            i += 1
        line_out += str(i) + char_processing
        line = line[i:]
    return line_out
             


print(runLength('aaabb'))
print(runLength('ab'))