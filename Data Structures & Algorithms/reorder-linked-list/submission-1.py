# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # use slow and fast pointer approach
        slow = fast = head

        # use fast and slow pointer approach to find middle of list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # find second half
        second_half = slow.next
        
        # seperate first half from second half
        slow.next = None

        second_half = self.reverseList(second_half)

        # weave the two halves together
        first_half = head # head serves as the anchor
        while second_half:

            # save temp lists for each half
            temp1 = first_half.next
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1

            # move lists forward
            first_half = temp1
            second_half = temp2
        

    def reverseList(self, head:Optional[ListNode]) ->Optional[ListNode]:
        
        prev,curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr

            curr = temp
        return prev




        
        