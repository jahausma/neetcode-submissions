class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        r = k - 1
        res = []

        while r <= len(nums)-1:
            temp = nums[l:r+1]
            n = max(temp)
            res.append(n)
            l+=1
            r+=1
        
        return res