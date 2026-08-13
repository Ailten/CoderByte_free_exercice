
# Two Sum (?).
# ?

# take an array, first element is the target, returl all pair of num who's sum make the target.

def func(arr: list):

    # extract target.
    target = arr[0]
    del arr[0]

    matches = set()
    for i in range(len(arr)):
        current_num = arr[i]
        num_match = target - current_num

        for j in range(i+1, len(arr)):
            num_compare = arr[j]

            # no match.
            if num_compare != num_match:
                continue

            # skip them self.
            if i == j:
                continue

            # order.
            if num_compare < current_num:
                (num_compare, current_num) = (current_num, num_compare)

            matches |= { (current_num, num_compare) }
            break

    if len(matches) == 0:
        return -1
    
    return '(' + ') ('.join([ f'{e[0]},{e[1]}' for e in matches ]) + ')'





print(func([7, 1, 3, 6, 9, 4, -2]))
print(func([7, 2, 3]))
print(func([4, 2, 2]))
print(func([4, 2]))
print(func([7, 5, 2, 5, 2]))
