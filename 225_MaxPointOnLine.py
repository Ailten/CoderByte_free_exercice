
# max pints on a line
# https://leetcode.com/problems/max-points-on-a-line/

def maxPoints(points: list[list[int]]) -> int:

    # return if zero or one points in list.
    if len(points) <= 1:
        return len(points)

    # remap as tuple (index, x, y).
    points_k: list[tuple[int, int, int]] = [(k, points[k][0], points[k][1]) for k in range(len(points))]

    # stock all group of same line.
    groups: list[set[tuple[int, int, int]]] = []

    # loop on every two points compination.
    for i in range(len(points_k)):
        i_k = points_k[i]
        for j in range(i+1, len(points_k)):
            j_k = points_k[j]

            # get groups already made with both point into.
            groups_with_both = [g for g in groups if (
                i_k in g and
                j_k in g
            )]
            if len(groups_with_both) >= 1:  # skip if find one group (is already a group made previously).
                continue

            # get dif of pos (represent the line trajectory).
            dif_x = j_k[1] - i_k[1]
            dif_y = j_k[2] - i_k[2]

            # debug.
            #a = [p[0] for p in points_k if (
            #    p != i_k and
            #    p != j_k and
            #    (
            #        (dif_x == 0 and i_k[1] == p[1]) or  # if line full orizontal or full vertical.
            #        (dif_y == 0 and i_k[2] == p[2]) or
            #        (  # same trajectory line (as i and j).
            #            dif_x != 0 and dif_y != 0 and
            #            (p[1] - i_k[1]) / dif_x ==
            #            (p[2] - i_k[2]) / dif_y
            #        )
            #    )
            #)]
            #print(f"{i_k[1]}:{i_k[2]} - {j_k[1]}:{j_k[2]} -> {a}")

            # get every other points matching the same trajectory line.
            points_in_same_line = [p for p in points_k if (
                p != i_k and
                p != j_k and
                (
                    (dif_x == 0 and i_k[1] == p[1]) or  # if line full orizontal or full vertical.
                    (dif_y == 0 and i_k[2] == p[2]) or
                    (  # same trajectory line (as i and j).
                        dif_x != 0 and dif_y != 0 and
                        (p[1] - i_k[1]) / dif_x ==
                        (p[2] - i_k[2]) / dif_y
                    )
                )
            )]

            # skip all group with only i and j on line (to mush case).
            if len(points_in_same_line) == 0:
                continue

            # create a new group.
            group = set(points_in_same_line + [i_k, j_k])
            groups.append(group)

    # no group, min value equal 2.
    if len(groups) == 0:
        return 2
    
    # get the max group length.
    bigest_grp = max(groups, key=lambda g: len(g))
    return len(bigest_grp)



print(maxPoints([[1,1],[2,2],[3,3]]))  # 3.
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # 4.
