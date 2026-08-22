# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []

        def dfs(node):
            if not node:
                arr.append("N")
                return 
            arr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(arr)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",") # split the input string
        self.i = 0 

        def dfs():  # no input necessary since we are using self.i to index into vals
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            root_val = int(vals[self.i])
            self.i += 1
            node = TreeNode(root_val)
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        