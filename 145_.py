
# Edit Word.
# https://leetcode.com/problems/edit-distance/

# take two string, the first need to become same as the second, return the amound of operation to cast it.
# as operation you can "add char (any type at any index)", "remove (any type at any index)", or "replace (any type)".
# hard way (bonus): replace can only be replace by another char in the current word (swap).


# WIP.
def func(w1:str, w2:str, is_debuging: bool=False) -> int:

    # make word as array (easily edited).
    arr_w1 = list(w1.lower())
    arr_w2 = list(w2.lower())

    edit_count = 0

    w1_sort = [ (k,ord(c)) for k,c in enumerate(arr_w1) ]
    w1_sort.sort(key=lambda e: e[1]*1000 + (1000-e[0]))  # order by letter, (and by index in second time, latest first).
    w2_sort = [ (k,ord(c)) for k,c in enumerate(arr_w2) ]
    w2_sort.sort(key=lambda e: e[1])

    # insert and pop.
    char_to_add = []
    w1_i = 0
    w2_i = 0
    while True:
        if w1_i >= len(w1_sort) and w2_i >= len(w2_sort):
            break

        char_w1 = float('inf') if w1_i >= len(w1_sort) else w1_sort[w1_i][1]
        char_w2 = float('inf') if w2_i >= len(w2_sort) else w2_sort[w2_i][1]

        if char_w1 == char_w2:
            w1_i += 1
            w2_i += 1
            continue
        if char_w1 < char_w2:  # need pop.
            arr_w1.pop(w1_sort[w1_i][0])
            w1_sort = [ e if e[0] <= w1_sort[w1_i][0] else (e[0]-1, e[1]) for e in w1_sort ]  # decal all key (before pop).
            w1_i += 1
            edit_count += 1
            if is_debuging:
                print(f'remv "{chr(char_w1)}" -> {"".join(arr_w1)}')
            continue
        if char_w1 > char_w2:  # need add.
            char_to_add.append((w2_sort[w2_i][0], chr(char_w2)))
            w2_i += 1
            continue
            #arr_w1.insert(w2_sort[w2_i][0], chr(char_w2))
            #w2_i += 1
            #if char_w1 != float('inf'):
            #    w1_sort = [ e if e[0] < w1_sort[w1_i][0] else (e[0]+1, e[1]) for e in w1_sort ]  # decal all key (before add).
            #edit_count += 1
            #if is_debuging:
            #    print(f'add  "{chr(char_w2)}" -> {"".join(arr_w1)}')
            #continue
    
    # make all add.
    char_to_add.sort(key=lambda e: e[0])
    for cta in char_to_add:
        arr_w1.insert(cta[0], cta[1])
        edit_count += 1
        if is_debuging:
            print(f'add  "{cta[1]}" -> {"".join(arr_w1)}')

    w1_char_to_swap = [ (
        k,
        c,
        [ i for i in range(len(arr_w2)) if arr_w2[i] == c ]  # all index can be move to.
    ) for k,c in enumerate(arr_w1) if c != arr_w2[k] ]

    while len(w1_char_to_swap) != 0:
        current_char = w1_char_to_swap[0]
        dest_can_be = [ e for e in w1_char_to_swap if e[0] in current_char[2] ]
        if len(dest_can_be) == 0:  # should be never call.
            raise Exception('Error, cant swap')
        optimal_dest = [ e for e in dest_can_be if current_char[0] in e[2] ]  # priorise dest who solv both.
        is_both_solv = len(optimal_dest) >= 1

        dest = dest_can_be[0] if not is_both_solv else optimal_dest[0]
        (arr_w1[current_char[0]], arr_w1[dest[0]]) = (arr_w1[dest[0]], arr_w1[current_char[0]])
        w1_char_to_swap.remove(current_char)
        if is_both_solv:
            w1_char_to_swap.remove(dest)
        else:
            dest_i = w1_char_to_swap.index(dest)
            w1_char_to_swap[dest_i] = (current_char[0], dest[1], dest[2])
        edit_count += 1
        if is_debuging:
            print(f'swap "{current_char[1]}" with "{dest[1]}" -> {"".join(arr_w1)}')

    return edit_count


#print(func('aaa', 'aaa', is_debuging=True))  # 0.
#print(func('aaaa', 'aaa', is_debuging=True))  # 1.  (add)
#print(func('aa', 'aaa', is_debuging=True))  # 1.  (remv)
#print(func('aab', 'aba', is_debuging=True))  # 1.  (swap)

print(func('horse', 'ros', is_debuging=True))  # 3.
print(func('intention', 'execution', is_debuging=True))  # 8.
print(func('acurate', 'acuchar', is_debuging=True))  # 5.
