# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # initialize a priority queue
        pq = []
        # initializing counter as unique id for each node
        counter = 0

        # iterate through each other list
        for i in lists:
            l = i
            # traverese through each list node
            while l:
                # push tuple(node.val, unique id, node)
                heapq.heappush(pq, (l.val, counter, l))
                counter += 1
                l = l.next
            
        
        # use dummy method for list building
        dummy = ListNode(0)
        curr = dummy

        while pq:
            # pop the val
            val, count, node = heapq.heappop(pq)
            
            # create new node
            temp = ListNode(val)
            curr.next = temp
            curr = curr.next

        return dummy.next