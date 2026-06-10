
# overlapind RDV.
#

# take a list of RDV (list of 2 int, start/ end), and return if there is RDV overlaping or not (False if at least 2 is overlaping).


def func(rdvs : list[list[int]]) -> bool:

    for i in range(len(rdvs) - 1):
        for j in range(i + 1, len(rdvs)):

            # (if explained).
            #
            # |------------|
            #        |-------------|
            # i0     j0    i1      j1
            #
            #        j0 <  i1
            #           and
            # i0        <          j1

            if rdvs[i][0] < rdvs[j][1] and rdvs[j][0] < rdvs[i][1]:
                return False
            
    return True




print('___________ v1')

print(func([[5, 10], [15, 20]]))            # True.
print(func([[5, 15], [10, 20]]))            # False.
print(func([]))                             # True.
print(func([[5, 10], [1, 20]]))             # False.
print(func([[5, 10], [15, 20], [25, 30]]))  # True.
print(func([[5, 30], [10, 20], [25, 35]]))  # False.
print(func([[25, 30], [10, 20]]))           # True.
print(func([[10, 20], [5, 15]]))            # False.


# -----------------> now, return the all RDV overlaping (a list of list (both RDV overlaping)) -> [[[5,15], [10,20]], ...]

def funcV2(rdvs : list[list[int]]) -> bool:

    output = []

    for i in range(len(rdvs) - 1):
        for j in range(i + 1, len(rdvs)):
            if rdvs[i][0] < rdvs[j][1] and rdvs[j][0] < rdvs[i][1]:
                output.append([rdvs[i], rdvs[j]])
            
    return output


print('___________ v2')

print(funcV2([[5, 10], [15, 20]]))            # [].
print(funcV2([[5, 15], [10, 20]]))            # [[[5, 15], [10, 20]]].
print(funcV2([]))                             # [].
print(funcV2([[5, 10], [1, 20]]))             # [[[5, 10], [1, 20]]].
print(funcV2([[5, 10], [15, 20], [25, 30]]))  # [].
print(funcV2([[5, 30], [10, 20], [25, 35]]))  # [[[5, 30], [10, 20]], [[5, 30], [25, 35]]].
print(funcV2([[25, 30], [10, 20]]))           # [].
print(funcV2([[10, 20], [5, 15]]))            # [[[10, 20], [5, 15]]].