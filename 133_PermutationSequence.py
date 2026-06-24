
# Permutation Sequence.
# https://leetcode.com/problems/permutation-sequence/



def func(n:int, k:int, value_sub: list[int] = []) -> str:

    dico_combination = {
        0: 0,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880
    }

    values = list(range(1, n+1))
    for vs in value_sub:
        if vs in values:
            values.remove(vs)

    if k == 0 or len(values) <= 1:
        return ''.join([ str(e) for e in values ])
    
    cases_first_val = dico_combination[len(values)-1]
    index_first_num = (k-1) // cases_first_val
    first_val = values[index_first_num]
    k = ((k-1) % cases_first_val)+1

    # ---> part who dont do what I expect.
    #value_sub.append(first_val)
    #return str(first_val) + func(n, k, value_sub)

    # ---> part who do what I expect.
    return str(first_val) + func(n, k, value_sub + [first_val])
    
    

print('< case 3 >')
print(func(3,1))  # 123
print(func(3,2))  # 132
print(func(3,3))  # 213
print(func(3,4))  # 231
print(func(3,5))  # 312
print(func(3,6))  # 321
print('< case 4 >')
print(func(4,1))  # 1234
print(func(4,6))  # 1432
print(func(4,7))  # 2134
print(func(4,8))  # 2143




print('< demo of memory parameter case >')

def func(edit:bool, my_list: list=[]) -> int:
    if edit:
        my_list.append('value')
    return len(my_list)

print(func(False, []))  # 0.
print(func(False))  # 0.
print(func(True))  # 1.
print(func(False))  # 1.  --> unexpected memory parameter.
print(func(False, []))  # 0.
print(func(False))  # 1.  --> default value still edited.



