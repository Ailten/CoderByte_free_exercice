
# reduce obj arr
# /

# take an array of object {'id': int, 'value': int} and return only those who as an unique id.


from functools import reduce

def mergeArr(arr: list[dict]) -> list[dict]:

    return reduce(lambda acc, b: 
        acc + ([b] if len([ a for a in arr if a['id'] == b['id'] ]) == 1 else [])
    , arr, [])



print(mergeArr([
    {'id': 1, 'value': 1},
    {'id': 2, 'value': 1},
    {'id': 2, 'value': 1},
    {'id': 3, 'value': 3}
]))