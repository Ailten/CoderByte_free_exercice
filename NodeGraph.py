

from typing import Optional

class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"]|None = None):
        self.val = val
        self.neighbors = neighbors if neighbors != None else []

    def __repr__(self) -> str:
        return f"(val : {self.val}, nei : {self.neighbors.__repr__()})"
    
    # ------>

    @staticmethod
    def fromList(list_int: list[list[int]]) -> Optional["Node"]:
        
        if len(list_int) == 0:
            return None
        
        list_node = [Node(val=i+1) for i in range(len(list_int))]
        for i in range(len(list_int)):
            current_node = list_node[i]
            for arr_index in list_int[i]:
                current_node.neighbors.append(list_node[arr_index-1])
        
        return list_node[0]
    
    def toList(self) -> list[list[int]]:
        list_node = self.getListOfAllNode()

        return [[nn.val for nn in n.neighbors] for n in list_node]
    
    # ------>

    def getListOfAllNode(self) -> list["Node"]:
        list_node = [self]
        index_incr = 0
        while True:
            current_node = list_node[index_incr]
            neighbors_index = current_node.neighbors
            for ni in neighbors_index:
                if ni in list_node:
                    continue
                list_node.append(ni)

            index_incr += 1
            if index_incr == len(list_node):
                break

        list_node.sort(key=lambda n: n.val)

        return list_node