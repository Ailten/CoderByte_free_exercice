
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

    while i < len(s) and j < len(s):
        
        is_j_increase = True

        #print('----')
        #print(dico_browse)
        #print(dico_pat)

        if is_dict_contains(char_taken, char_ask):

            if shortest_match == None or shortest_match[1]-shortest_match[0] > j-i:
                shortest_match = (i, j)

            is_j_increase = j != i

        current_char = None
        is_add = True

        if is_j_increase and j < len(s)-1:
            j += 1
            current_char = s[j]
        elif i < len(s)-1:
            i += 1
            current_char = s[i]
            is_add = False

        if current_char in char_ask:
            if is_add:
                if current_char in char_taken:
                    char_taken[current_char] += 1
                else:
                    char_taken |= {current_char: 1}
            else:
                char_taken[current_char] -= 1


    return "" if shortest_match == None else s[shortest_match[0]:shortest_match[j]]



print(func("ADOBECODEBANC", "ABC"))  # "BANK".
print(func("A", "A"))  # "A".
print(func("A", "AA"))  # "".