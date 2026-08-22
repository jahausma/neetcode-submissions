class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            m = (l + r)//2
            
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[m] == target:
                return m
            elif (nums[l] < target < nums[m]):
                r = m - 1
            elif (nums[m] < target < nums[r]):
                l = m + 1
            else:
                r -=1
                l +=1
        
        return -1

