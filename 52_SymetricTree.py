
# Symetric Tree (Medium).
# (?)

# take an array of binary info (child, parent), and determine if the tree binary is symetric or not.
# (vertion with input array of tuple, distinct values).


def symetricTree(arr) -> bool:

    dico = dict()

    # build tree binary into a dict of tuple.
    for e in arr:
        if not e[1] in dico:
            dico.update({e[1]: [e[0], None]})
        else:
            dico[e[1]][1] = e[0]
    
    # find the upper node.
    upper_index = None
    while True:
        upper = None
        for k, v in dico.items():
            if upper_index == None:
                upper = k
                continue
            if v[0] == upper_index or v[1] == upper_index:
                upper = k
        if upper == None:
            break
        upper_index = upper
    print(dico)
    
    # determine recursively if both side is simetry.
    return isTreeSimetry(dico, upper_index)




def isTreeSimetry(dico, index) -> bool:

    is_left_none = dico[index][0] == None or (not dico[index][0] in dico)
    is_right_none = dico[index][1] == None or (not dico[index][1] in dico)

    if is_left_none and is_right_none:
        return True
    if is_left_none != is_right_none:  # not sur if the right definition of simetry (maybe, implement rotation)
        return False
    return (
        isTreeSimetry(dico, dico[index][0]) and
        isTreeSimetry(dico, dico[index][1])
    )




# TODO: verify and edit this exercice (not working as I whant).

print(symetricTree([(1,2), (2,3), (4,2), (5,6), (6,3), (7,6)]))
print(symetricTree([(2,3), (4,2), (5,6), (6,3), (7,6)]))