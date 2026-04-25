
# Arith Geo (Easy).
# (?)

# return "arith" if the array send is an arythmetic suite, "geo" if it's geometrique, else return -1.




def arithGeo(arr):

    # can't be determined.
    if len(arr) <= 2:
        return -1

    last_dif = arr[1] - arr[0]
    is_arith = None
    is_geo = None
    patern_geo = None
    for i in range(2, len(arr)):
        current_dif = arr[i] - arr[i-1]

        # first loop, determine if 3 first number follow what rule.
        if i == 2:
            if last_dif == current_dif:  # FIXME: what should be done if is an arith of +0 ?
                is_arith = True
                continue
            patern_geo = arr[1] / arr[0]
            if patern_geo == arr[2] / arr[1]:  # FIXME: verify if there is other rule of geometry than multiply rule, like exponent.
                is_geo = True
                continue
            return -1

        if is_arith:
            if current_dif != last_dif:
                return -1
        else:  # else can be only is_geo.
            if patern_geo != arr[i] / arr[i-1]:
                return -1
            
    return 'arith' if is_arith else 'geo'
        




print(arithGeo([1,2,3,4]))
print(arithGeo([1,2,4,8,16]))
print(arithGeo([1,2,3,4, 0]))
print(arithGeo([1,2,4,8,16, 0]))