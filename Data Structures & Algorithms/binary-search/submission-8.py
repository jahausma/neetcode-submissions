class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # we can exploit the fact that the array is of distince integers sorted in ascending order

        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            mid = l + (r - l)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
 
        return res