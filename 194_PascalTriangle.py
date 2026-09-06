
# pascal triangle.
# https://leetcode.com/problems/pascals-triangle/


def generate(numRows: int) -> list[list[int]]:

    if numRows < 1:
        return []

    output = [[1]]

    for stage in range(numRows-1):

        last_stage = output[len(output)-1]
        new_stage = [ last_stage[i] + last_stage[i+1] for i in range(len(last_stage) -1) ]
        new_stage.insert(0, 1)
        new_stage.append(1)
        output.append(new_stage)

    return output


print(generate(1))  # [[1]].
print(generate(3))  # [[1],[1,1],[1,2,1]].
print(generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]].