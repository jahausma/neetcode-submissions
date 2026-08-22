"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # initialize dict, {None:None} prevents key errors when indexing with None
        oldToCopy = {None:None}

        curr = head
        while curr:
            # create clone node
            copy = Node(curr.val)
            # key: old node, value: clone node
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            # grab clone node
            copy = oldToCopy[curr]
            # set clone node.next = to clone_node indexed by old_node.next
            copy.next = oldToCopy[curr.next]
            # set clone_node.random = to clone_node indexed by old_node.random
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]