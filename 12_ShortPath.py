
# Short Path (hard).
# (?)

# make a function, take an array of 3 kind of data.

def func(arr):

    letters = arr[1:int(arr[0])+1]
    paths = arr[1+len(letters):]

    paths = { (p[0], p[2]) for p in paths }

    start = letters[0]
    end = letters[-1]

    path_try = set(start)
    while True:
        new_path_try = set()
        for p in path_try:
            last_char = p[len(p)-1]
            new_path_to_push = { p + ps[1] for ps in paths if ps[0] == last_char }
            list_to_end = [ ps for ps in new_path_to_push if ps[len(ps)-1] == end ]
            if len(list_to_end) > 0:
                return list_to_end[0]
            new_path_try |= new_path_to_push

            # can be optimised, in reducing path_find when two path get to the same char, OR when two path get to a char aleady visited in this try.

        path_try = new_path_try


print(func(['4', 'A', 'B', 'C', 'D', 'A-B', 'B-D']))
print(func(['3', 'A', 'B', 'C', 'A-B', 'B-A', 'B-C']))