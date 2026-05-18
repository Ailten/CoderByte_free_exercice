
# Max Rectangle On Graph (Medium).
# (-)

# On vous donne une liste d'entiers positifs représentant les hauteurs de barres adjacentes d'un histogramme (chaque barre a une largeur de 1). Vous devez trouver l'aire du plus grand rectangle possible formé par ces barres.



def maxRectangleOnGraph(graph: list[int]) -> int:

    # make a copy of graph, to pick on it (without alterate the main graph).
    graph_to_pick = [ (k, v) for k, v in enumerate(graph) ]
    graph_to_pick.sort(key=lambda e: e[1])

    max_rect_area = min(*graph) * len(graph)

    for i in range(1, len(graph_to_pick)):
        column = graph_to_pick[i]
        height = column[1]

        index_left = column[0]
        index_right = column[0] + 1
        while True:

            print(f'column: {column}')
            print(f'i: {index_left} _ {index_right}')

            # eval era.
            current_era = (index_right - index_left) * height
            if current_era > max_rect_area:
                max_rect_area = current_era

            is_left_can_extend = (
                (index_left - 1) >= 0 and
                graph[index_left - 1] >= height
            )
            is_right_can_extend = (
                (index_right) < len(graph) and
                graph[index_right] >= height
            )

            # can't no more extend.
            if not is_left_can_extend and not is_right_can_extend:
                break

            if is_left_can_extend:
                index_left -= 1
            if is_right_can_extend:
                index_right += 1
        
        return max_rect_area




print(maxRectangleOnGraph([2, 1, 5, 6, 2, 3]))  # 10  // because 5*5 = 10 on column 5-6.