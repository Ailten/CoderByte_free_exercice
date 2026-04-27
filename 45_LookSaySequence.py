
# Look Say Sequence (Medium).
# (?)

# take a number, and return the next one in the Conway suite (221 -> 2211).

def lookSaySequence(num):

    num_str = str(num)
    num_str_out = ''

    last_char = None
    amount_of_time = None
    for char in num_str:

        if last_char == None:
            last_char = char
            amount_of_time = 1
            continue

        if char == last_char:
            amount_of_time += 1
            continue
        else:
            num_str_out += str(amount_of_time) + last_char

            last_char = char
            amount_of_time = 1

    num_str_out += str(amount_of_time) + last_char
    return int(num_str_out)
            
        






print(lookSaySequence(1))
print(lookSaySequence(221))