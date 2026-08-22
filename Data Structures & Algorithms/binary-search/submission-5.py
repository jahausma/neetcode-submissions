class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (high + low)//2   # you cant just take the difference of the two, you find the total span and divide by 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:    # search upper half of range
                low = mid + 1
            else:          # search lower half of range
                high = mid - 1

        return -1