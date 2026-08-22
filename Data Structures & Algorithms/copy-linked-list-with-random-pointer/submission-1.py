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
        # enable factory function for dictionary
        # MOST IMPORTANT FEATURE, allows for dynamically allocating a node
        oldToCopy = collections.defaultdict(lambda: Node(0)) # allows for creating a new node if there is no node for a corresponding key 
        # oldToCopy = {None:None}, cant use this in combination with that
        oldToCopy[None] = None

        curr = head
        while curr:
            oldToCopy[curr].val = curr.val
            oldToCopy[curr].next  = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head] 

        