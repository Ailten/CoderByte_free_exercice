
# Populating next right pointers in each node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Node|None) -> Node|None:

    if root == None:
        return None

    stage = [root]
    while len(stage) != 0:
        stage[len(stage)-1].next = None
        for r_i in range(len(stage)-1):
            stage[r_i].next = stage[r_i + 1]
    
        # move to next stage (can be improve).
        new_stage = []
        for r in stage:
            if r.left != None:
                new_stage.append(r.left)
            if r.right != None:
                new_stage.append(r.right)
        stage = new_stage

    return root


n = Node(1)  # build the tree.
n.left = Node(2)
n.right = Node(3)
n.left.left = Node(4)
n.left.right = Node(5)
n.right.left = Node(6)
n.right.right = Node(7)
n = connect(n)  # --> call func.
print(n.next)  # verify.
print(f'{n.left.next.val} {n.right.next}')
print(f'{n.left.left.next.val} {n.left.right.next.val} {n.right.left.next.val} {n.right.right.next}')
# None
# 3 None
# 5 6 7 None