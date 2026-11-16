
# Find voyel square in 2D array letter.
# /


def findIndexSquare(arr_letter: list[list[str]]) -> tuple[int, int]|None:

    def isVoyel(char: str) -> bool:
        return char in 'aeiou'
    
    arr_voyel = [[isVoyel(c) for c in l] for l in arr_letter]

    for y in range(len(arr_voyel)-1):
        for x in range(len(arr_voyel[y])-1):
            if (
                arr_voyel[y][x] and
                arr_voyel[y+1][x] and
                arr_voyel[y][x+1] and
                arr_voyel[y+1][x+1]
            ):
                return (x, y)
    return None



print(findIndexSquare(
    [
        ['a','c','y','u'],  #....
        ['t','u','e','z'],  #.oo.  (1,1)
        ['p','i','a','o'],  #.oo.
        ['t','u','d','z']   #....
    ]
))
print(findIndexSquare(
    [
        ['a','c','y','u'],  #....  None
        ['t','s','e','z'],  #....
        ['p','i','a','o'],  #....
        ['t','u','d','z']   #....
    ]
))
print(findIndexSquare(
    [
        ['a','c','y','u'],  #....
        ['t','s','e','z'],  #....
        ['p','i','a','o'],  #..oo  (2,2)
        ['t','p','e','i']   #..oo
    ]
))
print(findIndexSquare(
    [
        ['a','i','y','u'],  #oo..  (0,0)
        ['e','o','e','z'],  #oo..
        ['p','i','s','o'],  #....
        ['t','u','e','i']   #....
    ]
))
