

# Copy linked list with random pointer.
# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: Optional[Node]) -> Optional[Node]:

    new_node_list = []

    # create new list of node (same value, not connected).
    current_node = head
    while current_node != None:
        new_node_list.append((
            Node(current_node.val),  # stock a new instance of the node.
            id(current_node)  # stock the memory index of the node it refer.
        ))
        current_node = current_node.next

    # connect to his next (and random).
    current_node = head
    i = 0
    while current_node != None:

        if i < len(new_node_list) -1:  # connect to the next index.
            new_node_list[i][0].next = new_node_list[i+1][0]

        if current_node.random != None:
            id_random = id(current_node.random)  # get the memory adress of the current's random.
            new_random = next([n for n in new_node_list if n[1] == id_random].__iter__())  # find new random.
            new_node_list[i][0].random = new_random  # connect to new random.

        current_node = current_node.next
        i += 1
        
    return new_node_list[0][0]
    




print('--- test 1 ---')
nodes = [  # make nodes.
    Node(7),
    Node(13),
    Node(11),
    Node(10),
    Node(1),
]
for i in range(len(nodes)-1):  # connect next.
    nodes[i].next = nodes[i+1]
nodes[0].random = None  # connect random.
nodes[1].random = nodes[0]
nodes[2].random = nodes[4]
nodes[3].random = nodes[2]
nodes[4].random = nodes[0]

result = copyRandomList(nodes[0])  # execute.

nodes_result = []
while True:
    if result == None:
        break
    nodes_result.append(result)
    result = result.next

for i in range(len(nodes)):
    n_base = nodes[i]
    n_copy = nodes_result[i]
    print(f'{n_base.val} != {n_copy.val} -> {(id(n_base) != id(n_copy))}')  # print comparation address memory.
