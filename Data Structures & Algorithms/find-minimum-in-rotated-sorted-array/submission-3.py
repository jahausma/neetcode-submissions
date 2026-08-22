class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r)//2

            # check if nums[m] < nums[r]
            if nums[m] < nums[r]:
                # if it is, nums[m] can still be a minimum
                r = m
            else:
                # nums[m] can not be a minimum so we exclude it
                l = m + 1
        
        return nums[l]