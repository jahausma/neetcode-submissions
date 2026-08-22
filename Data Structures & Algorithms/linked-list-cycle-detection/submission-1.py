# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # we can use a hash map to see if we have visited a node before
        visited = set()  # pair: pointer, value
        cur = head
        while cur:
            if cur in visited: # check if we have visited the current node
                return True

            visited.add(cur) # add the current node to the set
            
            cur = cur.next
        
        return False