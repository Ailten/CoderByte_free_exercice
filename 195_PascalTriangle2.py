
# pascal triangle 2.
# https://leetcode.com/problems/pascals-triangle-ii/


def getRow(row_index: int) -> list[int]:

    if row_index < 0:
        return []
    
    rows = [[1],[]]
    for i in range(0, row_index):

        last_stage = rows[i%2]
        new_stage = [ last_stage[i] + last_stage[i+1] for i in range(len(last_stage) -1) ]
        new_stage.insert(0, 1)
        new_stage.append(1)
        rows[1-(i%2)] = new_stage

    return rows[row_index%2]


print(getRow(3))  # [1,3,3,1].
print(getRow(0))  # [1].
print(getRow(1))  # [1,1].
