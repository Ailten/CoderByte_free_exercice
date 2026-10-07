
# clone graph
# https://leetcode.com/problems/clone-graph/


from NodeGraph import Node

def cloneGraph(node: Node|None) -> Node|None:

    if node == None:
        return None
    
    # get all node (on a list).
    list_node = node.getListOfAllNode()

    # clone node (ony value, not neibor).
    new_list_node = [Node(n.val) for n in list_node]

    # clone neibor.
    for i in range(len(list_node)):
        ln = list_node[i]
        nln = new_list_node[i]
        for neibor_ln in ln.neighbors:
            val_neibor = neibor_ln.val
            new_neibor = next([e for e in new_list_node if e.val == val_neibor].__iter__(), None)
            if new_neibor == None:
                raise Exception("neibor not found")
            nln.neighbors.append(new_neibor)
    
    return new_list_node[0]




n = Node.fromList([[2,4],[1,3],[2,4],[1,3]])
print(n.toList())  # debug if cast work.
n2 = cloneGraph(n)
print(n2.toList())  # debug clone (as list int to).

# debug instance distinct.
print("instance :")
print(f"n1 : {[id(e) for e in n.getListOfAllNode()]}")
print(f"n2 : {[id(e) for e in n2.getListOfAllNode()]}")

