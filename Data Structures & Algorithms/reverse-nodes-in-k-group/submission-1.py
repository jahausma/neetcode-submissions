# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head 
        groupPrev = dummy # Tracks the node right before the current k-group

        while True:

            kth = self.get_Kth_node(groupPrev, k) # find the kth node of this segment

            if not kth:
                break # there are less than k nodes left and we are done

            groupNext = kth.next # save the node right after this kth group

            # do standard list reversal
            prev = groupNext # Point the tail of this reversed group directly to groupNext
            curr = groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 4. Connect the previous group's tail to the new head of this reversed group
            # Before reversal, groupPrev.next was the head of the group (e.g., node 1)
            # After reversal, 'kth' becomes the new head of the group (e.g., node 2)
            temp = groupPrev.next  # Save the original head (which is now the group's tail)
            groupPrev.next = kth   # Link previous segment to the new head
            groupPrev = temp       # Move groupPrev forward to the tail of our finished segment
            
        return dummy.next
            


    def get_Kth_node(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        while curr and count < k:
            count += 1
            curr = curr.next
        
        return curr