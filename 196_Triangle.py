
# triangle
# https://leetcode.com/problems/triangle/


# sum every path, really eavy on performence with large triangle.
def minimumTotal(triangle: list[list[int]]) -> int:

    sum_stage = [ (0, triangle[0][0]) ]
    for stage_index in range(1, len(triangle)):
        stage = triangle[stage_index]
        new_sum_stage: list[tuple[int,int]] = []
        for i in range(len(stage)):
            val = stage[i]

            # merge with left father.
            vals_to_add = [ e for e in sum_stage if e[0] == i-1 ]
            for va in vals_to_add:
                new_sum_stage.append((i, val+va[1]))

            # merge with right father.
            vals_to_add = [ e for e in sum_stage if e[0] == i ]
            for va in vals_to_add:
                new_sum_stage.append((i, val+va[1]))
        
        sum_stage = new_sum_stage

    return min([ e[1] for e in sum_stage ])


print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # 11.