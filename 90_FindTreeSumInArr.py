
# find tree sum in arr
# /

# take an array of int, and an int expected,


def FindTreeSumInArr(arr: list[int], target: int, quantity_ask: int = 3) -> list[int]|None:

    arr.sort()
    path = [ {'keys':[k], 'sum':v } for k,v in enumerate(arr) if v < target ]

    for _ in range(1, quantity_ask):
        next_path = []
        for current_path in path:
            for k,v in enumerate(arr):
                if k in current_path['keys']:  # skip it self.
                    continue
                new_sum = current_path['sum'] + v
                if new_sum > target:  # skip over range target.
                    continue
                new_keys = current_path['keys'] + [k]
                next_path.append({
                    'keys': new_keys, 
                    'sum': new_sum
                })
        path = next_path
    
    # filter double.
    path = [ [arr[pk] for pk in p['keys']] for p in path if p['sum'] == target ]
    set_unique = set()
    for i in range(len(path)):
        p = path[i]
        p.sort()
        set_unique |= {'.'.join([str(n) for n in p])}
    path = [ [int(c) for c in u.split('.')] for u in set_unique ]


    return path  # nothing find.


print(FindTreeSumInArr([1,2,3,4,5,6,7], 7, 3))
print(FindTreeSumInArr([1,2,3,4,5,6,7], 5, 2))


# -----------> V2.


def FindTreeSumInArrV2(arr: list[int], target: int, quantity_ask: int = 3) -> list[int]|None:

    arr.sort()
    path = { str(a) for a in arr if a < target }

    for _ in range(1, quantity_ask):
        new_path = set()
        for p in path:
            unfold_p = [ int(up) for up in p.split('.') ]
            total_p = sum(unfold_p)
            for a in arr:
                if a in unfold_p:
                    continue
                if total_p + a > target:
                    continue
                new_unfold_p = unfold_p + [a]
                new_unfold_p.sort()
                new_path |= {'.'.join([ str(up) for up in new_unfold_p ])}
                
        path = new_path
    
    output = [ [ int(up) for up in p.split('.') ] for p in path ]
    output = [ p for p in output if sum(p) == target ]
    return output



print(FindTreeSumInArrV2([1,2,3,4,5,6,7], 7, 3))
print(FindTreeSumInArrV2([1,2,3,4,5,6,7], 5, 2))
