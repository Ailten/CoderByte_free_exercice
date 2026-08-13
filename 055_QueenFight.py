
# Queen Fight (Medium).
# (?)

# take an array of position, (pos of queen in chest game), and determined if there is two queen who can attaque eatch other.

def queenFight(arr):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            queen_one = arr[i]
            queen_two = arr[j]

            if queen_one[0] == queen_two[0]:  # verticaly alligne.
                return True
            if queen_one[1] == queen_two[1]:  # horizontaly alligne.
                return True
            
            dif_x = queen_two[0] - queen_one[0]
            if (
                queen_one[1] + dif_x == queen_two[1] or 
                queen_one[1] - dif_x == queen_two[1] 
            ):
                return True
            dif_y = queen_two[1] - queen_one[1]
            if (
                queen_one[0] + dif_y == queen_two[0] or 
                queen_one[0] - dif_y == queen_two[0] 
            ):
                return True
            
    return False


print(queenFight([ (0,0), (1,3), (-7,3) ]))  # True (vertialy).
print(queenFight([ (0,0), (1,2), (-7,3) ]))  # False.
print(queenFight([ (0,0), (1,1), (-7,3) ]))  # True (diagoaly).
print(queenFight([ (0,0), (1,-1), (-7,3) ]))  # True (other diagoaly).
print(queenFight([ (-7,0), (1,-1), (-7,3) ]))  # True (horizontaly).