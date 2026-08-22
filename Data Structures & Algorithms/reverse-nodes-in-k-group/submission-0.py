# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # check if there are k nodes left
        curr = head
        count = 0
        while curr and count < k:
            count += 1
            curr = curr.next
        
        # check base case (nodes left < k)
        if count < k:
            return head

        # standard string reversal up to kth node from head
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(curr, k)

        return prev
            