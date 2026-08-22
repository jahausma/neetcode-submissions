# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2

        carry = 0
        result = resultNode = ListNode(0)

        while curr1 or curr2:
            if curr1 and curr2:
                sum = curr1.val + curr2.val + carry
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                sum = curr1.val + carry
                curr1 = curr1.next
            elif curr2:
                sum = curr2.val + carry
                curr2 = curr2.next
            if sum >= 10:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            
            tempNode = ListNode(sum)
            print(sum)
            resultNode.next = tempNode
            resultNode = resultNode.next

        if carry:
            tempNode = ListNode(1)
            resultNode.next = tempNode
        
        return result.next
