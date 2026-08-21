
# Sort By Remove.
# /

# inspired from the stalin order.
def sortByRm(l: list[int]) -> list[int]:

    elements_removed = []

    # remove elemnt who mess the order.
    i = 1
    while i < len(l):
        if l[i-1] > l[i]:
            element_removed = l.pop(i)
            i -= 1

            index_to_place = None
            for j in range(len(elements_removed)):
                if element_removed < elements_removed[j]:
                    index_to_place = j
                    break
            if index_to_place == None:
                elements_removed.append(element_removed)
            else:
                elements_removed.insert(index_to_place, element_removed)

        i+=1

    # debug.
    #print(l)
    #print(elements_removed)

    # merge both list sorted.
    li = 0
    eri = 0
    while True:
        if li == len(l):
            l.extend(elements_removed[eri:])
            break
        if eri == len(elements_removed):
            break

        is_l_ordered = l[li] <= elements_removed[eri]

        # stay l element.
        if is_l_ordered:
            li += 1
            continue

        # insert from element removed.
        l.insert(li, elements_removed[eri])
        eri += 1
        li += 1

    return l



print(sortByRm([0,1,2,9,5,4,3,7,8,6]))  # [0,1,2,3,4,5,6,7,8,9].