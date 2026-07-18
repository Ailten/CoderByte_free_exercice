
# Combinations.
# https://leetcode.com/problems/combinations/


def func(n: int, k:int, exclude: list[int]=[]) -> list[list[int]]:

    if k > n:
        return []
    if k == n:
        return [[ e for e in range(1, n+1) if not e in exclude ]]
    if k == 1:
        return [ [e] for e in range(1, n+1) if not e in exclude ]

    combination = []
    
    num_maked = []
    for i in range(1, n+1):
        if i in exclude:
            continue

        num_maked.append(i)
        rest = func(n, k-1, exclude+num_maked)

        for r in rest:
            new_combination = [i] + r
            combination.append(new_combination)

    return combination


print(func(1, 1))  # [[1]].
print(func(2, 1))  # [[1],[2]].
print(func(2, 2))  # [[1,2]].
print(func(3, 2))  # [[1,2],[1,3],[2,3]].
print(func(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]].
#print(func(5, 3))  # [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]].

# conclusion.
# if K is 1, return all value from 1 to N in a list (eatch in a list).
# if K is N, return all value from 1 to N in a list (in a list).
# combination start by [ 1 to K ]
# combination end by [ N-K+1 to N]
# the amount of combination starting by the same first number decrease (due to reduction of combination valide).