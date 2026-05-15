
# Second Degree Equation (Medium).
# https://fr.wikipedia.org/wiki/%C3%89quation_du_second_degr%C3%A9

# resolve an equation from second degree.

import math

def secondDegreeEquation(a: int|float, b: int|float, c: int|float) -> int|float|None|tuple[int|float,int|float]:
    discriminant = b**2 - 4*a*c
    if discriminant > 0:  # two output.
        descri_sqrt = math.sqrt(discriminant)
        return (
            (-b-descri_sqrt) / 2*a,
            (-b+descri_sqrt) / 2*a
        )
    elif discriminant == 0:
        return -(b / 2*a)
    return None  # no result possible.

# ax² + bx + c = 0
# find x.
print(secondDegreeEquation(5, 2, 3))