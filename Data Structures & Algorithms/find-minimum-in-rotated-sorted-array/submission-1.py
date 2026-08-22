class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:

            # we check if array is already sorted and if it is,
            # we found the minimum and break
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            # compute the mid point
            mid = (l + r)//2
            res = min(res,nums[mid])
            # check if the left part is the sorted part and move left
            print(nums[mid])
            print(nums[l])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
                
        return res