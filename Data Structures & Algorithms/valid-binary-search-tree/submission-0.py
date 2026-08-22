# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs_valid(node, lowerBound, upperBound):
            if not node:
                return True

            if not (lowerBound < node.val < upperBound):
                return False
            
            return (dfs_valid(node.left, lowerBound, node.val) and dfs_valid(node.right, node.val, upperBound))

        return dfs_valid(root, float("-inf"), float("inf"))