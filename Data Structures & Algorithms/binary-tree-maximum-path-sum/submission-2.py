# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        globalMax = float("-inf")

        def dfs(node):
            nonlocal globalMax
            if not node: 
                return 0

            leftMax = max(0,dfs(node.left))
            rightMax = max(0,dfs(node.right))

            # check if max goes through current node
            globalMax = max(leftMax + rightMax + node.val, globalMax)

            return node.val + max(rightMax, leftMax)
        
        dfs(root)

        return globalMax
        