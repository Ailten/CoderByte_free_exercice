
# Bracket Combinations (hard).
# https://coderbyte.com/information/Bracket%20Combinations

def BracketCombinations(num):

    list_case = { '()' }

    for _ in range(2, num +1):
        new_list_case = set()
        for c in list_case:
            for j in range(0, len(c)):
                new_list_case |= { c[:j] + '()' + c[j:] }
        list_case = new_list_case

    return len(list_case)



# keep this function call here.
print(BracketCombinations(3))