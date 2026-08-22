class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        r = k - 1
        res = []

        while r <= len(nums)-1:
            temp = sorted(nums[l:r+1])
            res.append(temp[-1])
            l+=1
            r+=1
        
        return res