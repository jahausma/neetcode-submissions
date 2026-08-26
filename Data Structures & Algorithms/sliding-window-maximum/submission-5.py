class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0 

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val if out of window
            if l > q[0]:
                q.popleft()
 
            if (r + 1) >= k: # zero indexed so we add 1 to compare to k
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output



