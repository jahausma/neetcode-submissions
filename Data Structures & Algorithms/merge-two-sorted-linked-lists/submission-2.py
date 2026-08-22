# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # creating dummy listNode helps with edge case handling, it also
        # acts as an anchor for returning a linked list at the end
        dummy = node = ListNode()

        # 2: Loop through both curr1 and curr2 while they are not empty

        while list1 and list2:

            if list1.val < list2.val:
                node.next = list1    # set tail to smaller node 2
                list1 = list1.next   # advance curr2
            else:
                node.next = list2    # set tail to smaller node 1
                list2 = list2.next   # advance curr1
        
            node = node.next    # advance our tracking node
        
        # append the rest of which ever list is left over
        node.next = list1 or list2
        
        return dummy.next