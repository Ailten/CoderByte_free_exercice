
# String Calculate (Medium).
# (?)

# function who take a string, and execute a calcul ('one plus one' -> 3), can take number from 0 to 9, and do "plus" or "minus".


def stringCalculate(line: str) -> int:

    arr_word_num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "tree": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "height": 8,
        "nine": 9
    }

    line_arr = line.split()

    if len(line_arr) != 3:
        raise Exception('not valid line.')
    
    is_plus = line_arr[1] == 'plus'
    values = (arr_word_num[line_arr[0]], arr_word_num[line_arr[2]])
    return (
        values[0] + values[1]
        if is_plus else
        values[0] - values[1]
    )


print(stringCalculate('one plus zero'))
print(stringCalculate('tree minus one'))
print(stringCalculate('two plus one'))