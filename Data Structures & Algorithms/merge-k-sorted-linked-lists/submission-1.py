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
        for head in lists:
            if head:
                # push tuple(node.val, unique id, node)
                heapq.heappush(pq, (head.val, counter, head))
                counter += 1
                head = head.next
            
        
        # use dummy method for list building
        dummy = ListNode(0)
        curr = dummy

        while pq:
            # pop the val
            val, count, node = heapq.heappop(pq)
            
            # dynamically link to the next node
            curr.next = node
            curr = curr.next
            
            # check if node has a nearest neighbor
            if node.next:
                heapq.heappush(pq, (node.next.val, counter, node.next))
                counter +=1

    

        return dummy.next