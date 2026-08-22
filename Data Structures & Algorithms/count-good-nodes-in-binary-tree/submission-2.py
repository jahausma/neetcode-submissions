# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:

        m = root.val

        def dfs(node, m):
            if node:
                if node.val >= m: 
                    self.res+=1
                    m = max(m,node.val)
                if node.left:
                    dfs(node.left, m)
                if node.right:
                    dfs(node.right, m)

        if root.left:
            dfs(root.left,m)
        if root.right:
            dfs(root.right, m)
        
        return 1 + self.res