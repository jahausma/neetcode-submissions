# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # precompute hashMap for finding roots position in the inorder array (O(n) to O(1) optimization for lookup)
        indices = {val: idx for idx, val in enumerate(inorder)} # dictionary comprehension

        # keep global variable to keep track of what preorder index we are at
        self.pre_idx = 0
        def dfs(l, r):
            if l > r: # base case, means we have gone through entire array
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)




        