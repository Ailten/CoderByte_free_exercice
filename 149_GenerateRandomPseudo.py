
# random pseudo.
# /

# return a string, the string should be an odd length between 3 and 7, alernate of voyel and console, randomely.


import random

def func() -> str:

    #random.seed(myIntSeed)
    rand = random.Random()

    def get_random_letter(is_voyel: bool) -> str:
        voyel_ascii_value = {'a','e','i','o','u'}  # 'y' exclude.
        if is_voyel:
            voyels_list = list(voyel_ascii_value)
            voyel_picked = voyels_list[rand.randint(0, len(voyels_list)-1)]
            if voyel_picked == 'i' and rand.randint(0,99) < 15:  # 15% chance to cast 'i' to 'y'.
                voyel_picked = 'y'
            return voyel_picked
        all_ascii_value = { chr(c) for c in range(ord('a'),ord('z')+1) }
        consone_asccii_value = all_ascii_value - voyel_ascii_value
        consone_list = list(consone_asccii_value)
        consone_picked = consone_list[rand.randint(0, len(consone_list)-1)]
        return consone_picked

    pseudo = []

    is_next_are_voyel = rand.randint(0, 2) == 1
    
    length_pseudo = rand.randint(3, 7)
    for i in range(length_pseudo):
        current_char = get_random_letter(is_next_are_voyel)
        pseudo.append(current_char)
        is_next_are_voyel = not is_next_are_voyel

    return ''.join(pseudo)



print(func())
print(func())
print(func())



