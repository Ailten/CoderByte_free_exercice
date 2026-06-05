
#

def func(val: str) -> int:

    dict_rom_to_int = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'X': 10,
        'IX': 9,
        'L': 50,
        'XL': 40,
        'C': 100,
        'D': 500,
        'CD': 400,
        'M': 1000
    }

    output = 0

    while len(val) != 0:
        current_char = val[0]
        next_char = '' if len(val) < 2 else val[1]
        current_val = dict_rom_to_int.get(current_char + next_char)

        is_two_char = current_val != None
        if not is_two_char:
            current_val = dict_rom_to_int.get(current_char)

        if current_val == None:  # error, not found.
            return None
        
        output += current_val
        
        val = val[2:] if is_two_char else val[1:]
    return output


print(func('III'))  # 3
print(func('IV'))  # 4
print(func('CXV'))  # 115