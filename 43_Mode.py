
# Mode (Medium).
# (?)

# take an array of int, and return the value apearing the more frequently (if there are many time the same, return one of those).

def mode(arr):

    dico = dict()
    for e in arr:
        if not e in dico:
            dico.update({e: 1})
        else:
            dico[e] += 1
    arr_tuple = [ (k, v) for k,v in dico.items() ]
    arr_tuple.sort(key=lambda e: e[1], reverse=True)
    return arr_tuple[0][0]


print(mode([1,2,3, 1]))
print(mode([1,2,3, 2]))
print(mode([1,2,3, 3, 4,4]))