
# Remove Duble Arr Orderd.
# /

# take an array of numbers, remove duble, stay in same order.
# [0,0,1,1,4,1,3] -> [0,1,4,3,_,_,_]

def removeDuble(arr: list[int]) -> list[int|None]:

    arr_sanitize =  [ (
        a if len([ 1 for v in arr[:k+1] if v == a]) == 1 else None
    ) for k,a in enumerate(arr) ]
    arr_values = [ v for v in arr_sanitize if v != None]
    arr_values += [None] * (len(arr_sanitize) - len(arr_values))
    return arr_values

print(removeDuble([0,0,1,1,4,1,3]))  # 0,1,4,3,None,None,None