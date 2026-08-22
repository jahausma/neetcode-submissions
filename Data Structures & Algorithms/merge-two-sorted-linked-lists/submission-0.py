# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        curr1 = list1
        curr2 = list2

        # 2: Loop through both curr1 and curr2 while they are not empty

        while curr1 and curr2:

            if curr1.val < curr2.val:
                tail.next = curr1    # set tail to smaller node 2
                curr1 = curr1.next   # advance curr2
            else:
                tail.next = curr2    # set tail to smaller node 1
                curr2 = curr2.next   # advance curr1
        
            tail = tail.next    # advance our tracking tail
        
        # append the rest of which ever list is left over
        if curr1:
            tail.next = curr1
        else: 
            tail.next = curr2
        
        return dummy.next