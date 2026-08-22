# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:

        max = root.val

        def dfs(node, max):
            if node:
                if node.val >= max: 
                    self.res+=1
                    max = node.val
                if node.left:
                    dfs(node.left, max)
                if node.right:
                    dfs(node.right, max)

        if root.left:
            dfs(root.left,max)
        if root.right:
            dfs(root.right, max)
        
        return 1 + self.res