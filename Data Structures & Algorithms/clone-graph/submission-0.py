"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        def clone(node): # dfs for cloning graph
            if node in oldToNew:
                return oldToNew[node]

            # initialize a copy of the node
            copy = Node(node.val)
            # add the copy to the dictionary
            oldToNew[node]  = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node) if node else None # handles edge case of null node