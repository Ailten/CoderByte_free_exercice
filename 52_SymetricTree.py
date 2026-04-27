
# Symetric Tree (Medium).
# (?)

# take an array of binary info (shild, parent), and determine if the tree binary is symetric or not.


def symetricTree(arr):

    dico = dict()

    for e in arr:
        if not e[1] in dico:
            dico.update({e[1]: [e[0], None]})
        else:
            dico[1][1] = e[0]
    
    # ... continue.


print([(1,2), (2,3), (4,2), (5,6), (6,3), (7,6)])
print([(2,3), (4,2), (5,6), (6,3), (7,6)])