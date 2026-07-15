
# min window substring.
# https://leetcode.com/problems/minimum-window-substring/


from collections import Counter

def func(s: str, patern: str) -> str:

    if len(patern) == 0 or len(s) == 0:
        return ""

    shortest_match = None

    i = 0
    j = 0

    char_taken = dict()
    char_ask = dict(Counter(list(patern)))

    def is_dict_contains(base_data: dict, ask_data: dict) -> bool:
        for k,v in ask_data.items():
            if not k in base_data:
                return False
            if base_data[k] < v:
                return False
        return True

    while True:
        if i >= len(s) and j >= len(s):
            break
        
        #print('----')
        #print(f'i:{i}  j:{j}')
        #print(f'{s[i:j]}')

        is_j_increase = j < len(s)

        if is_dict_contains(char_taken, char_ask):

            if shortest_match == None or shortest_match[1]-shortest_match[0] > j-i:
                shortest_match = (i, j)

            is_j_increase = False

        if is_j_increase:
            j += 1
            char_taken |= {s[j-1]: char_taken.get(s[j-1], 0) +1}
        else:
            char_taken[s[i]] -= 1
            i += 1

    return (
        "" if shortest_match == None else 
        s[shortest_match[0]:shortest_match[1]]
    )



print("-- basic test")
print(func("A", "A"))  # "A".
print(func("ABCA", "BA"))  # "AB".
print(func("ADABCDBA", "AC"))  # "ABC".
print("-- errors test")
print(func("A", "AA") == "")  # True.
print(func("", "A") == "")  # True.
print(func("A", "") == "")  # True.
print("-- real test")
print(func("ADOBECODEBANC", "ABC"))  # "BANC".
print(func(".A.B..AB.A.B.", "AB"))  # "AB".
print(func(".A.B...B.A..", "ABA"))  # "A.B...B.A".